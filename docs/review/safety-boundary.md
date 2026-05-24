# Safety Boundary

This document outlines the safety mechanisms designed to prevent over-automation, unauthorized spending, and secret leakage.

## Decision Postures
The SDK classifies endpoints into explicit decision postures. **Classification is not authorization**, and **payment challenge detection is not payment approval**.

* `pay_and_verify`: A standard, supported settlement rail was detected. The runtime *may* execute this if local policy allows.
* `observe_only`: An agent commerce surface or post-settlement validator was detected. The runtime will *not* execute payment. 
* `stop_safely`: High-intent friction (e.g., `session` execution) or malformed payloads detected. Execution is halted.
* `reject_invalid`: Unparseable challenges. Ignored entirely.

## Secret Redaction Policy
Raw secrets (private keys, macaroons, preimages, grant tokens, shared payment tokens) are strictly stripped from all public evidence models, CLI outputs, and external telemetry payloads. This review package and associated mock payloads contain no real credentials.

## Review Questions
1. Does the SDK adequately prevent over-automation when encountering unknown payment intents?
2. Is the `stop_safely` behavior sufficient for malformed HATEOAS routing?
3. Are there edge cases where `observe_only` might leak into an execution path?
4. Does the secret stripping logic (e.g., `_strip_secrets_from_evidence`) miss any known credential containers?
5. Are local `PaymentPolicy` limits evaluated at the correct stage of the HTTP 402 negotiation loop?