# Case input / explicit assumptions

Synthetic case B. Planner creates request R1, which invokes model instance M1 on GPU D0. M1 emits call T1 to a tool; the tool result resumes R1 and M1 execution. Policy specific to this example: M1 weights remain resident, R1 KV is retained during tool wait, grows on resume and is released at completion. No other request executes on D0 in this case. Columns are states, not proportional durations. Concurrency and isolation guarantees are outside this single-request example.

This self-contained scenario was authored for this repository. It is not a published paper, a measured workload, or a claim about the user’s implementation. No external figure was used as a mechanism source.
