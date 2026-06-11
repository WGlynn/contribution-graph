# reference/

A runnable floor for the mechanism — the tractable-approximation tier of
`theory/foundation.md`, not the north star.

## `dri.py`

Derives a per-lane DRI table from a repo's git log. Stdlib only, no deps.

```bash
python dri.py --repo /path/to/repo
python dri.py --repo /path/to/repo --lane "auth=src/auth" --lane "api=src/api"
python dri.py --repo /path/to/repo --half-life-days 90
```

Weight = decay(commit age) x review-proxy, where review-proxy is 1.0 for merge
commits / co-authored commits and a small constant for bare direct pushes. DRI =
argmax weight per lane. Lanes default to top-level directories; override with
`--lane name=prefix` (path-glob, per `theory/04-granularity.md`).

## Honest limits (these are the point, not caveats)

- **Review signal is a proxy.** Git does not record code review; a merge commit
  is a stand-in. True reviewed-and-merged weighting needs the forge API. This is
  the cheap floor that still beats self-nomination.
- **Identity is naive.** It groups by raw `author name`. Real use needs identity
  resolution first — `.mailmap` consumption is an open TODO (see
  `failure-modes/05-identity-fragmentation.md`, which this code surfaced).
- **No Goodhart defense yet.** Reviewer-diversity weighting and revert-survival
  scoring (`failure-modes/02-goodhart.md`) are not implemented here.

The value of this file is that it *runs*, produces a sane table on real repos
(tested at 3,000+ commits), and exposes the gaps the prose hid.

## Next hardening (planned)

- **Split credit across touched lanes** (`08-cross-lane-gaming`): divide each commit's weight by the number of lanes it touches, so a wide mechanical sweep cannot farm ownership of many lanes. One-line change to the accumulation step.
