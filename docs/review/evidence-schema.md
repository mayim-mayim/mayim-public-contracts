# Evidence Schema

The SDK generates local and externally-reportable evidence containers. **Evidence is an observation, not proof of commercial success.**

## Semantic Fields
* `payment_performed`: Boolean indicating if the client runtime attempted a settlement.
* `payment_receipt_present`: Boolean indicating if the server returned a recognizable cryptographic receipt artifact. **Note:** The absence of a payment receipt should not be treated automatically as a failure, as cache semantics vary.
* `verification_status`: `verified` (client matched cryptographic proof), `unverified` (pure observation), or `self_reported` (client claims success without a verifiable artifact).
* `evidence_class`: Identifies the origin of the observation (e.g., `crawler_detected_402`, `self_reported_challenge`).

The schema explicitly decouples the detection of a surface (`protocol`, `network`, `asset`) from the actual execution state.

## Review Questions
1. Does the evidence schema clearly distinguish between an unexecuted observation and a failed payment?
2. Are the `verification_status` transitions logical for a buyer-side client?
3. Should additional metadata be stripped before an observation is considered public-safe?