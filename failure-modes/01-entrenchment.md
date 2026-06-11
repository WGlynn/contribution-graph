# Failure mode: entrenchment

**Attack / failure:** early contributors accumulate weight and lock out
newcomers permanently. The argmax never changes because the incumbent's
historical weight dwarfs any new entrant, even one now doing more current work.

**Why the naive mechanism is vulnerable:** an undecayed Σ of historical
contribution is monotonic in tenure. First mover wins forever.

**Defenses (composed):**
1. **Decay.** `decay(age(p))` with a half-life on the order of the project's
   activity period. Historical weight bleeds off; only contributors who keep
   working keep their lead. A half-life that is too long re-introduces
   entrenchment; too short makes ownership thrash. Tuning is per-project and is
   itself a public parameter.
2. **Re-derivation cadence T.** The table is recomputed every period, so a
   newcomer who out-contributes the incumbent *this* period can take the lane
   *next* period, not in some indefinite future.
3. **Opt-out, not opt-in for newcomers.** Lanes are assigned from the graph;
   a newcomer does not need anyone's permission to start accumulating weight in
   an unowned or under-maintained lane.

**Residual risk:** a contributor who games the half-life by doing just enough
to stay above decay threshold without real engagement. Partially caught by the
`quality` term (reviewed-merged, not raw), but a determined low-effort incumbent
is a real open problem. Flagged, not solved.
