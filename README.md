# contribution-graph

Mechanism design for **mechanically-allocated DRIs** — assigning ownership and
review responsibility from demonstrated contribution history instead of
self-nomination or politics.

> Whoever has actually shipped reviewed work in an area is the default owner of
> its triage lane. The assignment rule is auditable from git history, not vibes.


> **Read `theory/foundation.md` first.** This repo stands on a shared substrate that EF Deep Funding and the Contribution Compact established; it adds the *assignment* question and its hardening, with credit.

## The one distinction that makes this tractable

This is deliberately **not** a Shapley value computation. Shapley answers "how do
we fairly split a fixed surplus" — a *distribution* rule, O(2^n), needing a
defined coalition value. This answers "who should be routed to" — an *assignment*
rule, O(commits), needing only the contribution graph. They compose (Shapley can
distribute a reward pool *across* the DRIs this assigns) but they solve different
problems. Holding that line is what keeps the whole mechanism cheap and auditable.
See `prior-art/shapley.md` and `theory/01-influence-dag.md`.

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

- `theory/` — the mechanism (`foundation`, `00-mechanism`, `01-influence-dag`),
  the governance stance (`02-governance` — where judgment lives), and the
  political economy it encodes (`03-cooperative-capitalism` — compete on the
  surface, cooperate on the substrate)
- `failure-modes/` — adversarial analysis, one file per attack (8 of them) plus
  `THREAT-MODEL.md`, the attacker's-eye synthesis
- `prior-art/` — Shapley value, EF Deep Funding, the Contribution Compact, and
  where this differs (all fact-checked against source)
- `reference/` — `dri.py`, a runnable stdlib-only floor that derives a DRI table
  from any repo's git log

## License

MIT (intent: maximize adoption of the mechanism, not capture it).
