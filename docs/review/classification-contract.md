# Classification Contract

The `ln-church-agent` SDK acts as a buyer-side inspector. It must correctly classify incoming HTTP 402 challenges or metadata into actionable settlement rails or observational surfaces.

## Boundary Definitions

* **Executable Settlement Rails**: Standard payment flows that the SDK is authorized to negotiate (e.g., `L402`, `x402`, `MPP`).
* **Emerging Commerce Surfaces**: Higher-order protocols (e.g., `AP2`, `ACP`, `APP`) that dictate mandates, cart checkouts, or delegated tokens. These are strictly classified as `observe_only` or `inspect-only`.
* **Unmapped / Invalid**: Malformed challenges, unsupported draft shapes, or conflicting metadata.

## The Over-Classification Risk
A critical design philosophy is preventing over-classification. Looking "payable" is not sufficient to be deemed "payable." If a commerce protocol (like `AP2`) co-exists with a valid settlement rail (like `x402`), the SDK deliberately suppresses the `pay_and_verify` recommendation to prevent unauthorized mandate signing, defaulting to `observe_only`.

## Review Questions
1. Does the SDK over-classify endpoints as payable?
2. Are the boundaries between `invalid`, `unmapped`, `observed_only`, and payable surfaces reasonable?
3. Is `observe-only` as a default safe enough for emerging commerce surfaces?
4. What cases should remain `invalid` rather than becoming `observed_only`?
5. Are the emitted fields sufficient for later verification?