
# PoC: Transaction Input Bypass via Incomplete Validation (Pocketnet)

## Description

This PoC simulates the critical vulnerability where malformed transactions with missing `scriptSig` inputs bypass validation in `CheckTransaction()`.

## Files

- `run_poc.py`: Entry point to run the test.
- `validation.py`: Contains mocked logic simulating the vulnerable `CheckTransaction()` function.
- `malformed_tx.json`: A crafted transaction with missing `scriptSig`.
- `README.txt`: This file.

## How to Run

1. Open VS Code.
2. Unzip the folder.
3. Open a terminal inside the folder.
4. Run:

```bash
python3 run_poc.py
```

## Expected Output

```
✅ Bypassed validation for input 0: Missing scriptSig accepted!
✅ Transaction accepted — INVALID!
```

This confirms the vulnerable logic accepted an invalid transaction input.

## Severity: CRITICAL
