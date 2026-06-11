# Prior art: Deep Funding (Ethereum Foundation)

[deepfunding.org](https://www.deepfunding.org) · [github.com/deepfunding](https://github.com/deepfunding) —
Vitalik-originated, Ethereum-Foundation-backed (EF is a listed "Gardener"
collaborator; the rewards pool is ~$220k — ~$170k to repos, ~$50k to winning
models — across several orgs incl. Allo Capital and Pollen Labs, per
deepfunding.org as of 2026-06-11). It applies credit attribution to Ethereum's
open-source dependency graph, with Shapley as the conceptual fairness anchor
(the live mechanism is pairwise-jury distillation, see below — not a literal
Shapley computation).

> Disambiguation: this is **EF** Deep Funding, not the unrelated SingularityNET
> program of a similar name. Default any "deep funding" reference to EF's.

## The actual artifact (verified from the cloned repos)

- **The graph:** a depth-2 directed dependency graph rooted at Ethereum. The
  actual data file (`graph/unweighted_graph.json`) contains **34 seed (Level 1)
  nodes, 4,990 dependency (Level 2) nodes — 5,024 total — and 14,927 edges**.
  > Source discrepancy (verified 2026-06-11): Deep Funding's README *headline*
  > says "31 seed nodes, 5,024 dependency nodes, 14,927 edges." Two of those three
  > disagree with its own data file: the data has 34 level-1 nodes (and lists 34
  > seed repos under "How It Works"), and the 5,024 is the *total* node count, not
  > the dependency count (deps alone are 4,990). Only the 14,927 edge count
  > matches. This repo cites the data-file numbers and flags the headline.
- **The edge convention** (reused verbatim in `theory/foundation.md`): for an
  edge `source → target` (source = dependent, target = dependency), the weight is
  "the portion of the credit for `source` that belongs to `target`." Weights
  leaving a node **sum to less than one**; the remainder is the credit retained
  by the node itself. The edge format (Deep Funding's own illustrative example):
  ```json
  {"relation": "GOLANG", "weight": 0.1,
   "source": ".../prysm", "target": ".../go-multihash"}
  ```
  > Note: that `0.1` is Deep Funding's *format illustration*, not a computed
  > weight. In the shipped `unweighted_graph.json` every edge weight is `0` (it is
  > the blank graph competitors fill in). A real computed weight, from the example
  > weighted graph, is `prysm → ethereum = 0.0294`. Don't cite `0.1` as a result.
- **The scoring mechanism** (verified against deepfunding.org + the `scoring`,
  `jury-evaluation`, and `oss-evals` repos, 2026-06-11): "a market of AIs as the
  engine and humans as the steering wheel." Competitors submit a full set of edge
  weights (a model). A **human jury** answers **pairwise** spot-checks — *"has A
  or B been more valuable to Ethereum's success?"* — over a sample. A submission
  **"gets a higher score if it is more compatible with the spot-checks."** That is
  the whole scoring signal: alignment with sampled pairwise human judgment.
  > Honest limit: Deep Funding publishes the scoring *code* (`scoring` repo) and
  > the pairwise-jury framing, but the fetched pages do **not** state a single
  > fixed loss function (Spearman / log-loss / etc.). So this repo describes the
  > mechanism (pairwise-jury-alignment) and does **not** assert a specific formula.
- **Single-layer vs multi-layer scoring** (`scoring` repo, verified): a
  "single-layer" mechanism compares many items contributing to one outcome; a
  "two-layer (really three-layer)" mechanism compares dependencies of an outcome
  *and* dependencies of each dependency — the recursion this repo's influence-DAG
  section mirrors.

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
