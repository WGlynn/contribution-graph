# contribution-graph

Mechanism design for **mechanically-allocated DRIs** — assigning ownership and
review responsibility from demonstrated contribution history instead of
self-nomination or politics.

> Whoever has actually shipped reviewed work in an area is the default owner of
> its triage lane. The assignment rule is auditable from git history, not vibes.

## Why this repo exists

Open-source projects hit the same coordination wall: who decides what, who
reviews what, who owns which surface. The usual answers are self-nomination
(loudest wins) or maintainer fiat (doesn't scale). This repo isolates a third
option as a designed mechanism — derive ownership lanes from the contribution
graph itself — and works through its theory, failure modes, and defenses.

## Status

Design-stage. This is theory being hardened before it's code. Nothing here is a
commitment to any specific project's governance.

## Open design questions

- **Entrenchment.** Contribution-history assignment can lock in early movers.
  Candidate defense: lanes are opt-out-able and re-derived on a cadence (monthly),
  so the graph stays live rather than ossifying.
- **Goodhart.** Once contribution is the currency, contribution gets gamed.
  Candidate defense: weight by *reviewed-and-merged* work, not raw commit count.
- **Cold start.** A new contributor has no graph. How do lanes bootstrap without
  excluding newcomers? Open.
- **Granularity.** Lane = file path? subsystem? semantic area? Too fine = noise,
  too coarse = the same fiat problem.

## Layout

- `theory/` — the mechanism, its invariants, and the impossibility results it
  navigates around
- `failure-modes/` — adversarial analysis, one file per attack
- `prior-art/` — Shapley value, quadratic funding, reputation systems, and where
  this differs

## License

MIT (intent: maximize adoption of the mechanism, not capture it).
