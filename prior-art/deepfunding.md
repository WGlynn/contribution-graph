# Prior art: Deep Funding (EF) and Shapley credit attribution

[deepfunding.org](https://deepfunding.org) — Ethereum-Foundation-supported,
Vitalik-seeded, applying Shapley-axiom credit attribution to the open-source
dependency graph: given that project B depends on library A, how much of B's
value/funding should flow to A, recursively, across the whole graph.

## What this repo takes from it

- **The graph is the source of truth.** Credit (there: funding; here: ownership)
  derives from the observable dependency/contribution graph, not from petition.
- **Recursion is the honest model.** Influence is transitive; A enables B enables
  C, and a fair attribution decomposes back through the chain. See
  `theory/01-influence-dag.md`.
- **Shapley is the fairness anchor** even when you cannot afford to compute it
  exactly — it tells you what a correct attribution *would* satisfy, so an
  approximation can be judged against it.

## Where this repo diverges

Deep Funding solves a **distribution** problem (how should money flow through the
graph). This repo solves an **assignment** problem (who should be routed to for
review/triage). Same graph, same Shapley lineage, different question — and the
assignment problem tolerates a cheaper, heuristic answer because the cost of a
slightly-wrong DRI is a misrouted review, not a misallocated grant.

The two compose: a deep-funding-style distribution could pay out *across* the
DRIs this mechanism assigns.
