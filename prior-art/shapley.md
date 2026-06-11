# Prior art: Shapley value

Shapley value: the unique distribution of a coalition's surplus satisfying
efficiency, symmetry, null-player, and additivity. It answers *how to split*.
This mechanism answers *who to route to* — an assignment, not a distribution.

Key difference: Shapley needs a characteristic function v(S) defined over every
coalition S (exponential, and usually unknowable for software contribution).
The contribution-graph mechanism needs only observed merged work — linear in
commits, fully observable. The price is that it is a heuristic assignment, not a
fairness-theoretic optimum. That trade is correct for a routing problem where
the cost of a slightly-wrong DRI is low and the cost of computing Shapley is
prohibitive.
