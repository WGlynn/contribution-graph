# The shared substrate (start here)

This repo does not invent its foundation. It stands on a substrate that several
independent lines of work — Ethereum Foundation's Deep Funding, and a separate
proposal of mine, the Contribution Compact — already established. Their work is
as load-bearing as anything here. This document states the common ground first,
as equals, and only then names the specific question this repo adds.

## The five things the substrate already gives us

1. **Value is a weighted directed credit-graph, not a flat tally.** Contribution
   is edges, not line counts. Deep Funding makes this concrete: a depth-2
   dependency graph (34 seed / level-1 nodes, 4,990 dependency / level-2 nodes,
   5,024 total nodes, 14,927 edges) rooted at Ethereum. (Counts are from the
   actual graph data file; Deep Funding's README *headline* says "31 seeds /
   5,024 deps," which disagrees with its own data — see `prior-art/deepfunding.md`
   for the reconciliation.)

2. **An edge weight is a *fraction of the downstream's credit*, and the
   remainder stays upstream's own.** Deep Funding's exact convention: for an edge
   `source → target`, the weight is "the portion of the credit for `source` that
   belongs to `target`," and the weights leaving a node sum to **less than one** —
   the leftover is the credit that rests with the node itself. This is a clean,
   reusable primitive and we adopt it verbatim.

3. **Recursion is the honest model.** Deep Funding's "multi-layer" mechanism
   compares dependencies of an outcome *and* dependencies of each dependency.
   Influence is transitive; a correct attribution decomposes back through the
   chain. This repo's `theory/01-influence-dag.md` is the same recursion.

4. **Shapley is the fairness anchor even when you cannot afford to compute it.**
   It tells you what a correct attribution *would* satisfy, so any cheap
   approximation can be judged against it.

5. **Unobservable edges are recovered by distilling sampled human judgment.**
   This is Deep Funding's key move and the answer to a problem this repo had left
   open. The full graph is too large to label by hand; instead a human jury
   answers *pairwise* spot-checks ("has A or B been more valuable to Ethereum's
   success?") on a sample, and an open market of AI models competes to generalize
   those preferences across the whole graph, with submissions scoring higher the
   more compatible they are with the jury's spot-checks. (Deep Funding publishes
   the scoring code and the pairwise-jury framing; it does not publish a single
   fixed loss formula, so this repo does not assert one.) My Contribution Compact reaches the same end
   by a different route — cross-rater agreement as the quality signal, plus a
   peer challenge-response window with bonded stake. Same problem, two valid
   distillations.

## Three questions, one substrate, no hierarchy

The substrate above is shared. What differs is the *question asked on it*:

| Work | Question | Output |
|---|---|---|
| **Deep Funding (EF)** | **distribution** — how should funding flow through the graph? | per-edge funding weights |
| **The Contribution Compact** | **compensation** — what do AI labs owe users whose training data they consumed? | per-user epoch settlement |
| **This repo** | **assignment** — who should be routed to for review and triage of each area? | per-lane DRI |

These are siblings, not a hierarchy. None subsumes the others; they compose. A
Deep-Funding-style distribution could pay out *across* the DRIs this repo
assigns; the Compact's epoch settlement is the same shape applied to the
user-to-lab edge. The reason this repo can be O(commits) while Deep Funding
runs a whole jury market is only that the *assignment* question tolerates a
cheaper, heuristic answer — a misrouted reviewer costs a re-route, a misweighted
funding edge costs a misallocated grant.

## What this repo actually adds

Granting the shared substrate, this repo contributes exactly two things:

1. The **assignment** framing — turning the credit-graph into a *router* (who
   owns what) rather than a distributor (who gets paid).
2. The **adversarial hardening** of that specific use — the failure-mode set
   (entrenchment, Goodhart, cold-start, granularity) for ownership-routing, which
   the distribution and compensation framings do not all share.

Everything underneath those two is inherited, with credit, from the work in
`prior-art/`.
