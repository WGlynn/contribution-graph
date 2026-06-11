# Prior art: Deep Funding (Ethereum Foundation)

[deepfunding.org](https://www.deepfunding.org) · [github.com/deepfunding](https://github.com/deepfunding) —
Ethereum-Foundation-supported, Vitalik-seeded, applying Shapley-style credit
attribution to Ethereum's open-source dependency graph.

> Disambiguation: this is **EF** Deep Funding, not the unrelated SingularityNET
> program of a similar name. Default any "deep funding" reference to EF's.

## The actual artifact (verified from the cloned repos)

- **The graph:** a depth-2 directed dependency graph rooted at Ethereum — 31
  seed (Level 1) nodes, 5,024 dependency (Level 2) nodes, 14,927 edges.
- **The edge convention** (reused verbatim in `theory/foundation.md`): for an
  edge `source → target` (source = dependent, target = dependency), the weight is
  "the portion of the credit for `source` that belongs to `target`." Weights
  leaving a node **sum to less than one**; the remainder is the credit retained
  by the node itself. Example edge:
  ```json
  {"relation": "GOLANG", "weight": 0.1,
   "source": ".../prysm", "target": ".../go-multihash"}
  ```
- **Two pillars** (Vitalik's framing): *value-as-graph* (per-achievement credit
  attribution over the dependency graph) + *distilled human judgment* (an open
  AI-model market estimates edge weights; a human jury spot-checks a sample; the
  winning submission is the one most aligned with the jury).
- **Single-layer vs multi-layer scoring** (`deepfunding-scoring` repo): compare
  many contributors to one outcome, OR compare dependencies *and* dependencies of
  dependencies — the recursion this repo's influence-DAG section mirrors.

## What this repo takes

- the graph-is-truth principle, the fractional-edge-weight convention, the
  transitive-recursion model, Shapley as the fairness anchor, and — most
  importantly — the **sample-and-distill** answer to unobservable edges (a jury
  scores a sample, a model generalizes). See `theory/foundation.md`.

## Where this repo diverges

Deep Funding solves **distribution** (how funding flows). This repo solves
**assignment** (who gets routed to). Same graph, same lineage, different
question — and assignment tolerates a cheaper heuristic because a misrouted
reviewer costs a re-route, not a misallocated grant. They compose: a
Deep-Funding distribution could pay out across the DRIs this repo assigns.

## Lineage note

This is not arms-length prior art. The author worked in the Deep Funding line
directly before this and adjacent work; the methodology continuity is direct,
not coincidental.
