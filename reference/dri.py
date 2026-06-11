#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Reference implementation: derive per-lane DRIs from a git log.

This is the TRACTABLE-APPROXIMATION tier from theory/foundation.md, made
runnable. It uses only what `git log` exposes:

  weight(author, lane) = sum over commits c touching lane of
        decay(age_days(c)) * review_proxy(c)

  review_proxy(c) = 1.0 if c is a merge commit OR carries a Co-authored-by
                    trailer (proxies "went through review / collaboration"),
                    else BARE_WEIGHT (a plain direct push counts for little).

The HONEST GAP (stated, not hidden): true reviewed-and-merged signal lives in
the forge API (GitHub/GitLab review records), not in git. A merge commit is a
proxy, not proof. The forge-API version is the upgrade; this git-only version is
the cheap floor that still beats self-nomination. See theory/foundation.md.

Stdlib only. Usage:
  python dri.py [--repo PATH] [--half-life-days N] [--lane name=prefix ...]
"""
import argparse
import math
import subprocess
import time
from collections import defaultdict

BARE_WEIGHT = 0.15           # a direct unreviewed push is worth little
DEFAULT_HALFLIFE = 120.0     # days
SENT = "\x01C\x01"           # commit-record sentinel
FS = "\x02"                  # field separator


def git(repo, *args):
    return subprocess.run(["git", "-C", repo, *args],
                          capture_output=True, text=True, errors="replace").stdout


def lane_of(path, lanes):
    for name, prefix in lanes:
        if path.startswith(prefix):
            return name
    return path.split("/")[0] if "/" in path else "(root)"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=".")
    ap.add_argument("--half-life-days", type=float, default=DEFAULT_HALFLIFE)
    ap.add_argument("--lane", action="append", default=[],
                    help="name=prefix, repeatable; else lanes = top-level dirs")
    args = ap.parse_args()
    lanes = [tuple(s.split("=", 1)) for s in args.lane if "=" in s]

    now = time.time()
    halflife = max(1.0, args.half_life_days) * 86400.0

    fmt = SENT + "%H" + FS + "%an" + FS + "%at" + FS + "%P" + FS + "%s"
    log = git(args.repo, "log", "--pretty=format:" + fmt, "--name-only")

    weight = defaultdict(float)
    lane_authors = defaultdict(set)
    commits = 0
    for block in log.split(SENT):
        block = block.strip("\n")
        if not block:
            continue
        header, _, filelist = block.partition("\n")
        parts = header.split(FS)
        if len(parts) < 4:
            continue
        _h, author, at, parents = parts[0], parts[1], parts[2], parts[3]
        subject = parts[4] if len(parts) > 4 else ""
        is_merge = len(parents.split()) > 1
        co_authored = "co-authored-by:" in (subject.lower() + filelist.lower())
        proxy = 1.0 if (is_merge or co_authored) else BARE_WEIGHT
        try:
            age = now - float(at)
        except ValueError:
            continue
        dk = math.pow(0.5, age / halflife)
        touched = {lane_of(ln.strip(), lanes)
                   for ln in filelist.splitlines() if ln.strip()}
        for lane in touched:
            weight[(lane, author)] += dk * proxy
            lane_authors[lane].add(author)
        commits += 1

    rows = []
    for lane in sorted(lane_authors):
        ranked = sorted(((a, weight[(lane, a)]) for a in lane_authors[lane]),
                        key=lambda x: -x[1])
        dri, w = ranked[0]
        runner_w = ranked[1][1] if len(ranked) > 1 else 0.0
        rows.append((lane, dri, w, w - runner_w, len(lane_authors[lane])))

    print(f"# DRI assignment -- {commits} commits, half-life "
          f"{args.half_life_days:.0f}d, {len(rows)} lanes\n")
    print(f"{'lane':<30} {'DRI':<20} {'weight':>8} {'margin':>8}")
    print("-" * 70)
    for lane, dri, w, margin, n in rows:
        flag = "  <- contested" if (n > 1 and margin < 0.5 * w) else ""
        print(f"{lane:<30} {dri[:19]:<20} {w:>8.2f} {margin:>8.2f}{flag}")
    print("\nnote: weight uses merge/co-author as the review proxy; true review "
          "signal needs the forge API (theory/foundation.md). 'contested' = no "
          "clear owner, route to humans.")


if __name__ == "__main__":
    main()
