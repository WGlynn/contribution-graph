# Cooperative capitalism: compete on the surface, cooperate on the substrate

This repo is not value-neutral plumbing. It encodes a specific political-economic
stance, and naming it makes the design choices legible rather than smuggled. The
stance is **cooperative capitalism**: mutualize the floor, compete on the top.
A market works best when the substrate it runs on is a shared commons and the
competition happens on the surface above it. The contribution graph is one
instance of that shape; a financial protocol (a uniform-clearing-price batch
exchange) is another. Same philosophy, different substrate.

## The two halves, and why neither alone works

**The cooperative substrate — recognition as a mutualized commons.** The credit
graph is public and recomputable by anyone. Your reviewed-and-merged work is a
fact on a shared ledger, not a favor a gatekeeper may grant or withhold. This is
an *insurance pool for recognition*: it mutualizes the risk that your contribution
goes unseen, denied, or quietly captured by whoever controls the org chart. No one
has to trust a maintainer's memory or goodwill; the substrate remembers.

**The competitive surface — ownership is earned, not granted.** On top of that
commons, lane ownership (the DRI) is won competitively: it is the argmax of
demonstrated, decayed, reviewed contribution. You earn the right to triage and
first-review a lane by doing the most reviewed work in it, and you can lose it by
stopping (decay) or by someone out-contributing you. This is a free market in
contribution.

Each half fails alone, and the failure modes are symmetric:

- **Pure competition** (maintainer fiat, self-nomination, no shared ledger)
  collapses into *gatekeeper extraction*: whoever holds the keys captures the
  credit, and contribution is rent the gatekeeper collects. This is the world the
  repo's `prior-art` section is reacting against.
- **Pure cooperation** (everyone flatly "owns" everything, no earned ownership)
  collapses into *free-rider dilution*: with no one accountable for an area,
  nobody is, and the commons degrades. Bus-factor goes to zero while everyone
  nominally shares.

Cooperative capitalism is the claim that you can dissolve *both* failure modes at
once by putting them on different layers: the commons prevents gatekeeper
extraction (your work is publicly recognized), and the earned surface prevents
free-rider dilution (ownership is concentrated, decayed, and opt-out). The
economic filter and the fairness filter point the same direction instead of
trading off — that coincidence is the structural edge, not a happy accident.

## What keeps the competition productive: the prize is capped and non-political

A market only stays cooperative-at-the-substrate if winning the surface cannot buy
control of the substrate. That is why the single most load-bearing line in this
repo is: **the DRI gets triage and first-review, never roadmap authority.** The
prize for winning a lane is *work* (you review and route), not *power* (you do not
direct). Capping the prize at a duty rather than a dominion is what stops the
competitive surface from corroding into the political capture it was meant to
replace. Anyone who wants the fight over *direction* still has it — in the open,
as governance — and the mechanism refuses to launder that fight through "who is
technically the contributor."

This is the same move a well-designed exchange makes when it gives everyone a
single uniform clearing price: it removes the privileged position (the ordering
advantage, the gatekeeper's discretion) so that the only way to win is to bring
real value to the shared book, not to capture the rules of the book.

## Mechanism correspondences

The philosophy is not decoration; it maps onto specific mechanics already in this
repo and its sibling design:

| Cooperative-capitalist principle | In the contribution graph | In a batch-auction exchange (sibling) |
|---|---|---|
| Mutualized floor | public recomputable credit ledger | shared price discovery, treasury backstop |
| Earned, competitive top | lane ownership = argmax contribution | priority/arbitrage compete for surplus |
| No privileged position | one public computation, no reviewer fiat | uniform clearing price, no ordering edge |
| Honesty made structural | append-only credit, reverts net out (`06`) | dishonest reveal forfeits bond |
| Capped, non-extractive prize | DRI = duty (triage), not dominion (roadmap) | winning a batch ≠ controlling the venue |
| Fail-safe, not fail-capture | contested lanes route to humans (`THREAT-MODEL`) | circuit breakers halt, do not seize |

## Honest boundary

Cooperative capitalism is a stance, not a proof. This file does not claim the
mechanism is fair in some absolute sense; it claims the mechanism's *values are
explicit and its incentives are aligned with them*. The residual governance
(`theory/02-governance.md`) and the residual attacks (`THREAT-MODEL.md`) are where
the stance meets its limits, and both are stated rather than hidden. The point of
naming the politics is so a reader can disagree with the politics directly,
instead of discovering them later disguised as a technical default.
