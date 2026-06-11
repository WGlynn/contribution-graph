# The mechanism

## One sentence

Ownership of a maintenance lane defaults to whoever has the most
**reviewed-and-merged** work in that lane, re-derived on a fixed cadence from
the version-control graph, with opt-out.

## Formal statement

Let a project be partitioned into **lanes** L = {l_1 ... l_k} (a lane is a
review surface: a subsystem, a path glob, or a labeled area — granularity is a
design parameter, see below).

For each contributor c and lane l, define a **contribution weight**:

    w(c, l) = Σ over merged PRs p touching l, authored or reviewed by c, of
              decay(age(p)) · quality(p)

where:
- `decay(age)` is a half-life function (recent work counts more; a maintainer
  who stopped six months ago should not own a live lane forever).
- `quality(p)` weights **reviewed-and-merged** work above raw commits. A merged,
  reviewed PR scores; an unreviewed direct push or a self-merge scores near zero.
  This is the single most important term — it is the Goodhart defense (below).

The **DRI** (directly responsible individual) for lane l is:

    DRI(l) = argmax_c w(c, l)   — subject to c not having opted out

A public table maps lane → DRI → current weight, regenerated every period T
(proposed: monthly). The DRI is the default reviewer and triage owner for that
lane. They are not a gatekeeper with veto; they are who the system routes to
first, and who is accountable if the lane rots.

## What it is not

- **Not authority.** The DRI owns triage and first-review, not roadmap. Product
  decisions stay explicit and human, never assigned by graph. (This is the line
  that keeps the mechanism operational rather than political.)
- **Not permanent.** Re-derivation every T means the graph stays live. Stop
  contributing and the lane re-homes on its own.
- **Not self-nominated.** You cannot declare yourself owner; you can only become
  the argmax by doing the reviewed work. And you can always opt out.

## The three invariants

1. **Auditability.** Every assignment is recomputable from public git history by
   anyone. No private state, no maintainer fiat in the assignment step.
2. **Liveness.** ∂(assignment)/∂(recent contribution) > 0 and decay > 0, so the
   set of DRIs tracks who is *currently* doing the work, not who once did.
3. **Non-capture.** No single actor can become DRI of a lane they do not
   demonstrably maintain, because the weight is dominated by reviewed-merged
   work that requires *other people* to have approved it.

## Relationship to Shapley

This is deliberately *not* a Shapley value computation. Shapley answers "how do
we fairly split a fixed surplus among contributors" — it is a distribution rule.
This mechanism answers a different question: "who should be routed to" — an
assignment rule. Shapley is O(2^n) and needs a defined coalition value; this is
O(commits) and needs only the contribution graph. They compose (Shapley could
distribute a reward pool *across* the DRIs this mechanism assigns), but they
solve different problems. See `prior-art/shapley.md`.
