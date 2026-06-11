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

Weight = decay(commit age) x review-proxy / lanes-touched, where review-proxy is
1.0 for merge / co-authored commits and a small constant for bare direct pushes,
and the lanes-touched divisor splits a commit's credit across the lanes it edits
(`failure-modes/08`). DRI = argmax weight per lane. Lanes default to top-level
directories; override with `--lane name=prefix` (path-glob, per
`theory/04-granularity.md`).

## Honest limits (these are the point, not caveats)

- **Review signal is a proxy.** Git does not record code review; a merge commit
  is a stand-in. True reviewed-and-merged weighting needs the forge API. This is
  the cheap floor that still beats self-nomination.
- **Identity resolution is basic but real.** It uses `%aN`/`%aE`, so a repo
  `.mailmap` collapses aliases to a canonical name, with an email-cluster fallback
  for aliases not in the mailmap (`failure-modes/05-identity-fragmentation.md`,
  which this code surfaced and now closes). Cross-identity merge still needs a
  forge-side identity map for accounts sharing neither name nor email.
- **No Goodhart defense yet.** Reviewer-diversity weighting and revert-survival
  scoring (`failure-modes/02-goodhart.md`) are not implemented here — they need
  the forge API, not git alone. Stated, not hidden.

The value of this file is that it *runs*, produces a sane table on real repos
(tested at 3,000+ commits), and exposes the gaps the prose hid.

## Shipped hardenings (surfaced by running the code)

- **`.mailmap` + email-cluster identity** (`05-identity-fragmentation`): `%aN`/`%aE`
  collapse aliases; demonstrated to clear a false "contested" flag on a real repo.
- **Split credit across touched lanes** (`08-cross-lane-gaming`): each commit's
  weight is divided by the number of lanes it touches, so a wide mechanical sweep
  cannot farm ownership of many lanes.

## Still open (need the forge API, not git)

- Reviewer-diversity and revert-survival scoring (`02-goodhart`, `06-revert-war`).
- Cross-identity merge for accounts sharing neither name nor email.
