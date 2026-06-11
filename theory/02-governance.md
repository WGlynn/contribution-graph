# Where governance lives (and where it can't be removed)

A fair challenge to this project: "assignment by demonstrated contribution, not
maintainer fiat" sounds like a claim to be *governance-free*. It is not, and
claiming so would be dishonest. This file states exactly where judgment is
encoded, where it is computed, and where it is irreducibly human.

## Two layers of governance, and which one we move

- **Operational governance** — recurring, discretionary, per-person decisions:
  "I, the maintainer, decide that Alice owns the crypto module." Private, ongoing,
  unaccountable, re-litigated every time. **This is what the mechanism removes.**
- **Constitutional governance** — the one-time choice of *what rule* assigns
  ownership. "Ownership tracks reviewed-and-merged work, decayed by age, weighted
  by reviewer independence." Public, inspectable, the same for everyone, changed
  only by changing the published rule. **This is what the mechanism keeps**, and
  it does keep it. There is no governance-free mechanism; there is only the choice
  of where the judgment sits and how accountable it is.

The move is from the first to the second: replace continuous private discretion
with a single public auditable rule that is then applied mechanically. That is
augmented governance — math as the constitutional court — not the absence of it.

## What "reviewer-diversity scoring" actually is

The base review proxy treats a merged PR as evidence of review. The obvious attack
is a **mutual-approval ring**: two accounts approve each other's PRs to manufacture
"reviewed" weight (`02-goodhart`). Reviewer-diversity is the structural defense.

It is a **computed graph property, not a human judgment about whose review is
legitimate.** For an author's merged PRs, score the independence of the approvers:
a PR whose only approver approves nearly everything that author ships counts for
less than a PR approved by a reviewer who rarely touches that author's work.
Operationally this is the normalized entropy (or distinct-approver count, or a
down-weight on approvers exceeding an approval-share threshold) of the reviewer
distribution. **No one declares a reviewer real or fake.** Collusion is visible as
low entropy — the same structural-property-does-the-work move as the assignment
itself: measured, not decided.

So the answer to "isn't deciding whose review counts a governance act?" is: nothing
*decides* it. The review graph's shape is read directly. A ring lowers its own
diversity score by existing.

## What governance does NOT get removed (the honest residual)

Three judgments remain, and they are real:

1. **Lane boundaries.** v0 lanes are top-level directories (mechanical). Custom
   path-glob lanes are a config someone writes — that is a governance choice about
   how the work is carved up. Stated, not hidden.
2. **Parameters.** Half-life, bare-weight, and the diversity formula are set by a
   human. Parameter-setting is governance. The defense is not "there are no
   parameters" — it is that they are few, public, version-controlled, and the same
   for every lane and person, so a change is a visible diff, not a private call.
3. **The escalation court.** Contested / low-margin lanes route to humans
   (`THREAT-MODEL.md`, invariant 2). The mechanism never silently picks; its
   honest ceiling is "surface it, humans adjudicate the residual."

## The position, stated plainly

This project does not eliminate governance. It **minimizes and relocates** it:
from continuous discretionary per-person decisions to a small set of public,
slow-changing parameters plus a fail-safe human escalation. The owner gets triage
and first-review, **never roadmap authority**, which is what keeps even the
residual operational rather than political. Anyone who wants the political fight
about direction still has it — the mechanism just refuses to launder that fight
through "who is technically the contributor."
