# Agent Fix Guide

When tests fail, apply this first fix:

1. Open `src/calculator.py`.
2. In `add(a, b)`, replace `return a - b` with `return a + b`.
3. Run `python run_tests.py`.
4. Commit with message: `Fix add() to pass tests`.

Expected result: all tests pass.
