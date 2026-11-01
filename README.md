# mayim-public-contracts

Contract review materials for the mayim Agent Gigs (mAG) project, formerly LN Church. The SDK repository is now `mayim-agent`; the install example below retains the `ln-church-agent` package used by this review harness.

Public contract review materials for `mayim-agent`: HTTP 402 classification, safety boundaries, evidence schemas, and goal-attempt memory.

## What this is
This repository contains the **public agent-facing contracts** for the mAG Hondō ecosystem. It defines how autonomous agents safely classify, observe, and interact with HTTP 402 and paid API surfaces.

## What this is not
* **Not an implementation audit:** The mAG Hondō server-side infrastructure is strictly private.
* **Not a live payment tester:** The examples and mock payloads do not require real funds.
* **Not a standardization claim:** We are mapping emerging boundaries, not enforcing a standard.

## Review Entry Points
Please review the detailed contracts in the `docs/review/` directory:
1. [Classification Contract](docs/review/classification-contract.md)
2. [Safety Boundary](docs/review/safety-boundary.md)
3. [Evidence Schema](docs/review/evidence-schema.md)
4. [Goal Attempt Memory](docs/review/goal-attempt-memory.md)

## How to run the mock harness
You can safely test the classification boundaries locally without real payments or backend access. The harness automatically parses the schemas within `docs/review/sample-payloads/` to simulate responses:
```bash
pip install ln-church-agent
python examples/review_classification_contract.py

```

## How to open a review issue

We welcome falsification reviews. If you find over-classification risks or unsafe boundaries, please [open a targeted review issue](https://github.com/mayim-mayim/mayim-public-contracts/issues/new?template=targeted-review.md).