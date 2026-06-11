# Failure mode: identity fragmentation

**Surfaced by the reference implementation, not by theory.** Running
`reference/dri.py` against a real repo immediately exposed it: one human commits
under several git identities (`wglynn`, `Will Glynn`, `William Glynn` — different
`user.name`/`user.email` across machines and times). The mechanism treats each as
a distinct contributor.

**Why it breaks the mechanism:**
- **Self-dilution.** A person's weight in a lane is split across their aliases, so
  the true owner can lose the argmax to someone with a single consistent identity.
- **False contestation.** A lane genuinely owned by one person reads as
  "contested" because their two identities sit at rank 1 and rank 2 — the exact
  artifact observed on the first real run.
- **Inverse abuse.** The mirror image of Goodhart: an actor could *deliberately*
  fragment identity to dodge accountability, or consolidate aliases to inflate.

**Defenses:**
1. **Identity resolution before weighting.** Collapse aliases to a canonical
   contributor first. Git already has the mechanism: a `.mailmap` file maps
   name/email variants to one canonical identity, and `git log --use-mailmap`
   honors it. The reference impl should consume `.mailmap` (open TODO in the code).
2. **Email-domain + commit-signature clustering** for aliases not in `.mailmap`:
   same verified GPG key or same email across names is near-certain one person.
3. **Forge-account linkage** in the upgrade tier: the GitHub/GitLab API ties all
   a user's commits to one account regardless of local git identity, dissolving
   the problem entirely. This is one more reason the forge-API tier
   (theory/foundation.md) is the real target and the git-only floor is a floor.

**Residual:** an adversary who fragments across genuinely unlinkable identities
(distinct keys, distinct emails, no forge account) cannot be auto-merged. There
the mechanism degrades to flagging suspiciously-correlated aliases for human
review, not silently trusting them.

**Provenance note:** this failure mode is in the repo because the reference
implementation was *run*, not just written. Building surfaced what prose did not.
