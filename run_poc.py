
import json
from validation import check_transaction

def run_poc():
    with open("malformed_tx.json") as f:
        tx = json.load(f)
    check_transaction(tx)

if __name__ == "__main__":
    run_poc()
