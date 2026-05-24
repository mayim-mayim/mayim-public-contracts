# Reviewer Questions

Thank you for reviewing the `ln-church-agent` public contracts. We are looking for falsification, unsafe assumptions, unclear contracts, and missing edge cases. 

*Pick one section. You do not need to review the whole project.*

### Classification Reviewer
* Does the SDK over-classify endpoints as payable?
* Are the boundaries between `invalid`, `unmapped`, `observed_only`, and payable surfaces reasonable?

### Security Reviewer
* Are there edge cases where `observe_only` might leak into an execution path?
* Does the secret stripping logic miss any known credential containers?
* Does the SDK adequately prevent over-automation when encountering unknown payment intents?

### Agent Evaluation Reviewer
* Is `goal_attempt` a useful observation unit for agentic workflows?
* Should `unassessed` attempts be preserved?
* Is the schema strictly observational, or does it drift into recommendation/routing?

### Observability Reviewer
* Does the evidence schema clearly distinguish between an unexecuted observation and a failed payment?
* Are the emitted fields sufficient for later verification?

### Python SDK Reviewer
* Are local `PaymentPolicy` limits evaluated at the correct stage of the HTTP 402 negotiation loop?
* Are the mock harnesses and testing methodologies sound for validating the public API without hitting live infrastructure?