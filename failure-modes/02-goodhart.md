# Failure mode: Goodhart (the metric becomes the target)

**Failure:** once contribution-weight assigns ownership, contributors optimize
the weight, not the project. Commit-splitting, trivial-PR farming, review-trading
rings ("I approve yours, you approve mine").

**Defenses:**
- **Reviewed-and-merged, not raw.** Raw commit count is trivially farmable;
  reviewed-merged requires another party. Defeats solo commit-splitting.
- **Reviewer diversity.** Weight review-credit by the diversity of reviewers, not
  the count. A 2-person mutual-approval ring produces low diversity and earns
  little. (Open: the exact diversity function; entropy over reviewer identity is
  a candidate.)
- **Merged-impact, not merged-count.** A PR's quality term can scale with lines
  durably surviving (not later reverted) and with whether it closed a real issue.
  Harder to farm than PR count.

**Residual:** a sophisticated collusion ring with genuine reviewer diversity is
not fully defeated by any of these. The honest position: this raises the cost of
gaming above the cost of just doing the work, which is the realistic goal — not
unbreakability.
