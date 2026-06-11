# Prior art: The Contribution Compact

The author's own prior proposal (gist: WGlynn/7251d0791b9b474e90d47646d5c1a2da),
the **compensation** sibling on the shared substrate.

## What it solves

The unpriced externality where users of frontier AI labs are simultaneously
customers and uncompensated training-data contributors. Labs track revenue
*from* users but treat value *received* through training data as zero. The
Compact is the missing compensation layer: contribution compounds indefinitely
while access stays bounded by subscription, so the ledgers are misaligned.

## Mechanism (same substrate, compensation question)

- **Signal scope:** explicit RLHF feedback only (thumbs, regenerate, accept) —
  bounded, already-tracked.
- **Attribution:** per-action weight from rarity (novelty) x quality
  (cross-rater agreement) x freshness (recent signal favored). This is the same
  graph-edge-weight idea as Deep Funding, applied to the user → model edge.
- **Settlement:** quarterly epochs, threshold-gated payout (credit / revenue
  share / equity); below-threshold incurs no penalty.
- **Verification:** peer challenge-response with bonded stake, disputable in a
  fixed window before epoch close — the Compact's answer to the unobservable-edge
  problem, parallel to Deep Funding's jury distillation.
- **Sybil resistance:** stake-bonded pseudonyms; multi-account cost scales
  linearly, making bot-farms uneconomic.

## Relationship to this repo

Same substrate (value-as-credit-graph, fractional edge weight, Shapley anchor,
sampled-judgment distillation), different question: the Compact asks
*compensation* (what is owed), this repo asks *assignment* (who is routed to).
The Compact's epoch-settlement and the repo's lane-DRI are two outputs of one
shared attribution layer.
