# Failure mode: cross-lane gaming (breadth-farming and drive-by claims)

**Attack:** the per-lane weighting invites two breadth attacks the single-lane
failure modes miss:
- **Breadth-farming** — spread shallow touches across many lanes to become DRI of
  several at once. A mechanical sweep (a formatting pass, a dependency bump, a
  license-header insert) touches twenty files across twenty lanes in one commit
  and, if each touch scores equally, registers twenty ownership claims for one act
  of no ownership.
- **Drive-by claim** — touch a file in a lane you do not work in purely to plant a
  weight, diluting the real owner's margin and manufacturing a false "contested"
  flag that routes a settled lane to human review (a denial-of-routing attack).

**Why per-commit-per-lane equal credit backfires:** it treats "touched 20 lanes
once" as identical to "owns 20 lanes," when the first is almost always a sweep.

**Defenses:**
- **A commit's credit is split across the lanes it touches, not replicated.** A
  commit touching one lane gives that lane full weight; a commit touching twenty
  lanes gives each a twentieth. Breadth is penalized exactly because genuine
  ownership is concentrated and sweeps are diffuse. (Reference impl: change
  `weight[(lane,a)] += dk*proxy` to divide by `len(touched)` — a one-line edit;
  this is the next reference-impl hardening, noted in `reference/README.md`.)
- **The merge/review proxy already filters drive-bys.** A drive-by direct push
  scores `BARE_WEIGHT`; to plant real weight an attacker must get reviewed-and-
  merged into a lane they do not work in, which is the review wall doing its job.
- **A manufactured "contested" flag fails safe, not open.** The worst outcome of a
  drive-by is that a lane routes to a human, who sees a one-touch claimant against
  an established owner and dismisses it. Routing-to-human is the safe terminal
  state (same as `06-revert-war`), so this attack costs the attacker a reviewed
  merge to achieve a human shrug.

**Residual:** split-credit slightly under-rewards the rare legitimate cross-cutting
refactor that genuinely touches many lanes with depth. The position taken: that is
the correct bias. Cross-cutting work should accrue ownership where it is *repeated*,
not from a single wide commit; a real refactorer who keeps working a lane catches
up within a few re-derivation cycles.
