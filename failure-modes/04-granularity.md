# Failure mode: lane granularity (the partition problem)

**The tension:** a lane is a review surface, and how you cut the project into
lanes determines everything.

- **Too fine** (lane = file): noise. Ownership thrashes, every rename re-homes a
  lane, and the DRI table is unreadable.
- **Too coarse** (lane = whole repo): you have re-invented the single-maintainer
  bottleneck the mechanism was meant to dissolve.

**Design positions (not yet resolved):**
- **Path-glob lanes** (`src/auth/**`): cheapest and most legible, but track
  directory structure rather than semantic structure. A feature spanning three
  directories has no clean lane.
- **Label lanes** (issues/PRs tagged `area:retrieval`): track semantic structure
  but require human labeling discipline, re-introducing a manual step.
- **Derived lanes** (cluster the file co-change graph: files that change together
  are one lane): track *actual* coupling and need no manual step, but are opaque.
  Contributors cannot predict which lane a change lands in.

**Current lean:** path-glob lanes for v0 (legible, zero-overhead), with derived
lanes as the research direction once there is enough history to cluster on.
Granularity is a published per-project parameter, not a fixed constant.
