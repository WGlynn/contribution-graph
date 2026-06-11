# The influence-DAG refinement (north star vs tractable approximation)

## The flaw in flat attribution

The base mechanism (`00-mechanism.md`) weights a contributor by the merged PRs
they authored or reviewed in a lane. That is **flat** attribution: credit lands
on the commit author. But real contribution is a DAG of influence, not a list of
commits:

- the person who filed the issue that defined the problem
- the reviewer whose one comment changed the whole design
- the author of the primitive/module the PR was built on top of
- the maintainer who shaped the convention the PR follows

Flat attribution credits the typist and erases the chain. A contribution graph
that wants to find the *real* owner of a lane has to see the chain.

## The ideal: recursive Shapley over the influence DAG

Model contribution as a directed graph where an edge a → b means "a's work
enabled or shaped b's." The fair credit for any node decomposes **recursively**:
b's value flows partly back to its in-edges, and theirs to theirs. This is a
Shapley value computed over the influence DAG rather than over a flat set — it
captures inspiration and enabling chains that flat commit-counting cannot.

> Footnote (precision): "Shapley over the DAG" is, named exactly, the **Myerson
> value** — the Shapley value of the graph-restricted game, where only
> coalitions connected in the graph create value (`v(S)` summed over the
> connected components of `S`). Plain Shapley assumes any subset can form a
> coalition; the Myerson value is the right primitive when value only flows along
> the edges, which is precisely the influence-DAG case here.

This is the north star. It is also, in full generality:
- **expensive** (Shapley is exponential; the DAG is large),
- **partly unobservable** (the "one review comment that changed everything" is
  not a labeled edge in git), and
- **gameable** (manufacture influence edges to harvest credit).

## The tractable approximation, and why it is honest

The deployed mechanism approximates the influence DAG with two cheap, observable
proxies:

1. **Reviewed-and-merged weighting** captures one influence edge for free: the
   reviewer → author edge. A merged-with-review PR encodes that at least one
   other person shaped or vouched for the work. This is why `quality(p)` leans
   so hard on review: review *is* a recorded influence edge.
2. **Built-on-top-of** can be approximated by file/import dependency: a PR that
   modifies a module credits, at a discount, the lane that owns that module's
   core. One hop, not the full recursion, but it catches the largest enabling
   edges.

The gap between the north star and the approximation is stated, not hidden. The
mechanism does not claim to compute fair influence credit; it claims to be a
cheap, auditable router whose proxy correlates with influence well enough to
beat self-nomination and fiat. When the gap matters (a high-stakes lane, a
disputed assignment), fall back to human judgment — the mechanism routes the
default, it does not adjudicate the edge case.

## Lineage

This recursive-influence framing comes out of the deep-funding line of work on
Shapley-based credit attribution for open-source dependency graphs (see
`prior-art/deepfunding.md`). That work asks "how should funding flow through the
influence DAG"; this repo asks "who should be routed to" — the same DAG, a
different question on it. Holding that distinction (assignment, not distribution)
is what keeps the mechanism O(commits) instead of O(2^n).
