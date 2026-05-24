# Goal Attempt Memory

v1.10.0 introduces Day 1 Goal Attempt Observation. This represents what an agent attempted to accomplish for a declared goal, serving as a foundational data lake for behavioral memory.

## Architectural Stance
This is an explicit-only observation path. It is **not** recommendation, routing, recipe generation, or automatic provider selection. 

## Unassessed States
We explicitly preserve `unassessed` attempts (where `outcome` is omitted). Attempts that cannot currently be classified as success or failure are preserved so they can be reinterpreted by future evaluation functions.

## Step Classification
Execution steps are clearly demarcated as `free`, `paid`, `mixed`, `observe_only`, or `simulated` to calculate accurate reasoning cost estimations.

## Review Questions
1. Is `goal_attempt` a useful observation unit for agentic workflows?
2. Should `unassessed` attempts be preserved, or do they pollute the memory model?
3. Are `free` / `paid` / `mixed` / `observe_only` / `simulated` steps clearly separated?
4. Is this still observational, or does it drift into recommendation/routing?
5. What data should not be stored for privacy or safety reasons within a goal context?