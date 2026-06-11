# Failure mode: the ownership map is an attack map

**The tension with invariant 1 (auditability).** The mechanism publishes
lane → DRI. For a security-sensitive project that means publishing "this single
named person is the decision-maker and first-reviewer for the cryptography
module." That is a phishing target, a social-engineering map, and a
single-point-of-failure advertisement, handed to attackers for free. Auditability
(every assignment recomputable by anyone) and target-hardening (do not advertise
who owns the crown jewels) pull in opposite directions.

**This is sharpest exactly where the mechanism is most useful** — high-stakes,
security-conscious, accountable projects. The same property that makes the
assignment trustworthy (it is public and recomputable) makes the owner a target.

**Resolution: separate the computation from the published output.**
- **The computation stays public.** Anyone can run the mechanism over the public
  git history and verify that the assignment is correct. Invariant 1 is satisfied
  at the level of *method*, not *disclosure*.
- **The output identity is redactable per-lane sensitivity.** For a lane flagged
  sensitive, publish the *shape* (owned vs needs-owner, the weight distribution,
  the bus-factor) without publishing the *name*. The owner is known to the
  maintainers and recomputable by anyone with the contributor-identity mapping;
  it is simply not broadcast next to "crypto module."

**Honest cost:** this genuinely weakens auditability for sensitive lanes — a
third party without the identity mapping can verify the *method* but not the
*assignee*. That is a real trade, not a free lunch. The position taken here is
that for security-sensitive lanes, target-hardening outranks public name
disclosure, and method-auditability is the part of invariant 1 worth keeping
absolute. Non-sensitive lanes stay fully public, name included.
