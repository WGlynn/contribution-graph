# Failure mode: cold start (newcomers have no graph)

**Failure:** a capable new contributor has zero contribution weight everywhere,
so the mechanism never routes to them, so they never accumulate weight: a
self-reinforcing exclusion.

**Why it is not as bad as it looks:** the mechanism assigns *default routing*,
not *permission*. A newcomer does not need to be DRI to contribute; they open
PRs into any lane, those get reviewed and merged, and weight accrues. The DRI
is who gets routed to first, not who is allowed in.

**Defenses for the genuine gap (under-maintained lanes):**
- **Unowned lanes are open invitations.** A lane whose top weight is below a
  floor is marked "needs owner" and surfaces to newcomers as the lowest-barrier
  entry point.
- **Mentorship edges.** A newcomer's early PRs reviewed by an existing DRI create
  a recorded reviewer to author influence edge that benefits *both*: the DRI's
  review-diversity and the newcomer's weight. Onboarding becomes weight-positive
  for the mentor, aligning incentives.

**Open:** bootstrapping a brand-new project where *no one* has a graph yet. There
the mechanism degrades gracefully to "whoever shows up," which is the status quo;
it adds value as the graph fills, not on day zero.
