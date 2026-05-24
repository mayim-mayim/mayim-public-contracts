# Public Contract Review Package

LN Church Hondō is operated as a private implementation. This directory exposes reviewable public contracts only: classification boundaries, safety policies, evidence schemas, and goal-attempt observation models. The purpose of this review package is not to audit private infrastructure. It is to falsify whether the public agent-facing contracts are safe, clear, and useful for autonomous agents interacting with HTTP 402 / paid API surfaces.

## Scope of Review

We are soliciting targeted technical reviews to identify falsifications, unsafe assumptions, unclear contracts, and missing edge cases in our boundary definitions.

**In Scope:**
* Classification of HTTP 402 challenges vs. Agent Commerce surfaces.
* Safety boundaries (`observe_only`, `stop_safely`, `pay_and_verify`).
* Evidence schema structures and public metadata extraction.
* Goal-attempt memory models (unassessed vs. assessed states).

**Out of Scope:**
* Implementation audits of the private Hondō (server-side) infrastructure.
* Standardization claims (we are tracking standards, not establishing them).
* Endorsement of the economic viability of specific endpoints.
* Real payment testing with live funds.

## Reading Guide

Depending on your expertise, please review the relevant documents:
1. **[Classification Contract](classification-contract.md)**: How the SDK maps incoming challenges to settlement rails or commerce surfaces.
2. **[Safety Boundary](safety-boundary.md)**: How the SDK prevents unsafe automation and secret leakage.
3. **[Evidence Schema](evidence-schema.md)**: How observations are safely structured without exposing credentials.
4. **[Goal Attempt Memory](goal-attempt-memory.md)**: How behavioral traces are logged prior to outcome verification.
5. **[Reviewer Questions](reviewer-questions.md)**: A categorized list of falsification prompts to guide your review.
6. **[Sample Payloads](sample-payloads/)**: Mock JSON data representing these contracts.