# Failure mode: revert-war (retroactive weight destruction)

**Attack:** if quality scales with "lines durably surviving" (the Goodhart
defense in `02-goodhart.md`), an adversary can *revert a rival's merged work* to
retroactively tank the rival's lane weight, or revert-and-reauthor to transfer
credit. The metric that defends against farming becomes a weapon against rivals.

**Why the naive fix backfires:** crediting "surviving lines" makes credit
mutable after the fact, so anyone with merge access can rewrite history's credit
by reverting.

**Defenses:**
- **Credit is earned at merge time, not revoked by later reverts.** A
  reviewed-and-merged PR scores when it merges. A later revert does not subtract
  the original author's weight; it credits the *reverter* only if the revert is
  itself reviewed-and-merged with a stated cause. Credit is append-only.
- **Reverts net out against their own reverts.** A revert that is itself reverted
  (revert-war churn) cancels, leaving the original credit intact and flagging the
  pair of actors for review.
- **Revert-without-cause is low-weight.** A revert whose review comment does not
  reference a defect, a test failure, or an issue scores at `BARE_WEIGHT` — it
  looks like an unreviewed direct push, because that is what an unjustified revert
  is.

**Residual:** two maintainers in a genuine revert-war is a social conflict the
graph *surfaces* (the churn and the canceled credits are visible) but does not
*adjudicate*. The mechanism's job is to make the war legible, not to declare a
winner. Escalation to humans is the correct terminal state, not a failure of it.
