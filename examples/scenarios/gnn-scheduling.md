# Case input / explicit assumptions

Synthetic case A. Job J has operators a→b and a→c. A GNN encoder produces features; a predictor combines them with device conditions for C1 / GPU A and C2 / GPU B. Each predicted record contains symbolic time ti and memory mi, not measurements. The scheduler receives both records, checks feasibility and its objective, and selects C2 by this case assumption. Only J on GPU B executes. GPU A remains an unselected candidate. No accuracy, optimality or speedup claim is made.

This self-contained scenario was authored for this repository. It is not a published paper, a measured workload, or a claim about the user’s implementation. No external figure was used as a mechanism source.
