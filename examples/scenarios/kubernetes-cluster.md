# Case input / explicit assumptions

Synthetic case C. One Kubernetes cluster contains a research Resource controller, Kubernetes API, worker N1 with a training Pod, CPU, GPU A and local SSD, and worker N2 with an inference Pod, CPU and GPU B. The controller submits placement intent to the API; dotted mappings describe Pod placement. Shared storage supplies model weights to the inference Pod. Local SSD is accessed by the training Pod. The node interconnect is an abstract physical link with no measured bandwidth or exact network topology. Control-plane placement is intentionally not expanded. GPUs are exclusively assigned in this example; no MPS/MIG or sharing policy is implied. Kubernetes is a text platform title because no official logo input was supplied.

This self-contained scenario was authored for this repository. It is not a published paper, a measured workload, or a claim about the user’s implementation. No external figure was used as a mechanism source.
