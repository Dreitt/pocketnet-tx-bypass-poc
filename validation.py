
def check_transaction(tx):
    # Simulates the vulnerable CheckTransaction() logic in Pocketnet
    if not tx.get("vin"):
        raise ValueError("No inputs (vin) provided")

    for idx, vin in enumerate(tx["vin"]):
        # Vulnerable check: allows empty scriptSig if 'prevout' is set
        if "scriptSig" not in vin and "prevout" in vin:
            print(f"✅ Bypassed validation for input {idx}: Missing scriptSig accepted!")
            continue
        elif "scriptSig" not in vin:
            raise ValueError(f"❌ Invalid input {idx}: Missing scriptSig and no prevout")

    print("✅ Transaction accepted — INVALID!")
