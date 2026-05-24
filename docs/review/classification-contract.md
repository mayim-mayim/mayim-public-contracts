# Classification Contract

The `ln-church-agent` SDK acts as a buyer-side inspector. It must correctly classify incoming HTTP 402 challenges or metadata into actionable settlement rails or observational surfaces.

## Boundary Definitions

* **Executable Settlement Rails**: Standard payment flows that the SDK is authorized to negotiate (e.g., `L402`, `x402`, `MPP`).
* **Emerging Commerce Surfaces**: Higher-order protocols (e.g., `AP2`, `ACP`, `APP`) that dictate mandates, cart checkouts, or delegated tokens. These are strictly classified as `observe_only` or `inspect-only`.
* **Unmapped / Invalid**: Malformed challenges, unsupported draft shapes, or conflicting metadata.

## Terminology: Distinct States

To ensure rigorous analysis, the public contracts strictly distinguish between runtime decisions and empirical data qualities:

* **`observe_only` (Decision Posture)**: A runtime constraint applied by the SDK. When a commerce surface or unsupported constraint is detected, the agent transitions to this posture, ensuring it logs telemetry but **never** signs mandates or dispatches funds automatically.
* **`observed_only` (Observation Quality)**: A state assigned to an item within the historical corpus or telemetry lake. It indicates that a payment-like surface or raw 402 challenge was empirically discovered, but no settlement proof was generated and no actual payment was performed.

## The Over-Classification Risk
A critical design philosophy is preventing over-classification. Looking "payable" is not sufficient to be deemed "payable." If a commerce protocol (like `AP2`) co-exists with a valid settlement rail (like `x402`), the SDK deliberately suppresses the `pay_and_verify` recommendation to prevent unauthorized mandate signing, defaulting to the `observe_only` posture.

## Review Questions
1. Does the SDK over-classify endpoints as payable?
2. Are the boundaries between `invalid`, `unmapped`, `observed_only` (corpus quality), and payable surfaces reasonable?
3. Is `observe_only` as a default decision posture safe enough for emerging commerce surfaces?
4. What architectural edge cases should remain classified as `invalid` rather than becoming an `observed_only` trace in the corpus?
5. Are the emitted classification fields sufficient for asynchronous backend verification?