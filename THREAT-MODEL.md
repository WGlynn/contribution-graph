# Threat model

The failure-mode files each take one attack in isolation. This is the
attacker's-eye synthesis: what an adversary wants, what they can do, which defense
answers it, and what residual risk survives. The mechanism is not claimed
unbreakable — it is claimed *legible*: every residual ends at "route to a human,"
never at "silently assigns the wrong owner and hides it."

## Attacker goals

| Goal | Vector | Primary defense | Residual |
|---|---|---|---|
| Seize a lane I don't earn | self-nomination | assignment is computed from merged history, not claimed | none at mechanism level; social pressure on maintainers persists |
| Keep a lane after I stop contributing | stale dominance | time-decay + periodic re-derivation + opt-out (`01`) | a contributor active *just* enough to refresh decay; surfaced as low-margin |
| Inflate my weight cheaply | commit-count farming | reviewed-and-merged proxy + reviewer-diversity, not raw count (`02`) | merge/co-author is a *proxy*; true signal needs forge API (stated gap) |
| Destroy a rival's weight | revert-war (`06`) | credit is append-only; reverts net out; unjustified revert scores bare | a genuine two-maintainer war; surfaced as churn, escalated to humans |
| Split a rival's weight | identity fragmentation / drive-by (`05`,`08`) | `.mailmap` + email-cluster; split-credit across touched lanes | aliases sharing neither name nor email; rare cross-cutting refactor under-rewarded |
| Claim many lanes at once | breadth-farming (`08`) | per-commit credit split across its lanes | legitimate wide refactor catches up over cycles, not instantly |
| Block a settled lane (DoS routing) | manufactured "contested" (`08`) | fails safe — routes to a human who dismisses a one-touch claim | costs a human a glance |
| Turn the map into a target | publish who owns crypto (`07`) | computation public, output-identity redactable per-lane sensitivity | weakens auditability for sensitive lanes — a stated trade, not free |
| Game the area boundaries | granularity (`04`) | path-glob areas v0; co-change-derived areas as research | coarse areas hide sub-owners until the research tier lands |

## The two invariants every defense preserves

1. **Auditability** — every assignment is recomputable by a third party from public
   history. Weakened *only* for `07`-flagged sensitive lanes, and there only at the
   level of published *identity*, never published *method*.
2. **Fail-safe routing** — when the mechanism is unsure (low margin, contested,
   manufactured conflict), it routes to a human. It never silently picks. Every
   residual above terminates here, which is why "the graph surfaces it, humans
   adjudicate" is the honest ceiling and not a dodge.

## What is explicitly out of scope

- **Roadmap authority.** The owner gets triage and first-review, never decision
  power over direction. Most governance-capture attacks are out of scope because
  there is no governance prize to capture.
- **Sybil identity creation** at the forge level (fake accounts passing review).
  That is the host platform's account-integrity problem; this mechanism assumes
  the forge's identity layer, it does not replace it.
