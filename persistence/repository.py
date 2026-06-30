import json
import os

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Data')
JSON_FILE = os.path.join(DATA_DIR, 'customers.json')
BIN_FILE = os.path.join(DATA_DIR, 'summary.bin')



os.makedirs(DATA_DIR, exist_ok=True)

# --- JSON FORMAT ---
def save(bank):
    
    accounts_data = [account.get_info() for account in bank._accounts.values()]
    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(accounts_data, f, indent=4)

def load():
    if not os.path.exists(JSON_FILE):
        return []
    
    try:
        with open(JSON_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# --- BINARY FORMAT ---
def export_summary(bank):
    total_accounts = len(bank._accounts)
    total_balance = sum(account.balance for account in bank._accounts.values())
    
    
    summary_text = f"Total Accounts: {total_accounts} | Total Bank Balance: ${total_balance:,.2f}"
    data_bytes = bytearray(summary_text, "utf-8")
    
    with open(BIN_FILE, "wb") as f:
        f.write(data_bytes)

def import_summary():
    if not os.path.exists(BIN_FILE):
        print("No binary summary found.")
        return
        
    file_size = os.path.getsize(BIN_FILE)
    buffer = bytearray(file_size)
    
    with open(BIN_FILE, "rb") as f:
        f.readinto(buffer)
        
    print(f"\n[Binary Summary Read]: {buffer.decode('utf-8')}")
