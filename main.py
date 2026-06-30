import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from entities.savings_account import SavingsAccount
from entities.checking_account import CheckingAccount
from entities.premium_account import PremiumAccount
from entities.bank_account import BankAccount
from logic.bank import Bank
from persistence.repository import save, load, export_summary, import_summary
from exceptions.errors import BankError

def show_menu():
    print("""
╔══════════════════════════════════╗
║           SMART BANK             ║
╠══════════════════════════════════╣
║  1. Create savings account       ║
║  2. Create checking account      ║
║  3. Create premium account       ║
║  4. Deposit                      ║
║  5. Withdraw                     ║
║  6. Transfer                     ║
║  7. View audit history           ║
║  8. Balance ranking              ║
║  9. Generate bank report         ║
║ 10. Save data                    ║
║ 11. Load data                    ║
║  0. Exit                         ║
╚══════════════════════════════════╝
""")

def main():
    print("--- METHOD RESOLUTION ORDER (MRO) ---")
    print(PremiumAccount.__mro__)
    print("-------------------------------------\n")
    print("Welcome to Smart Bank Management System")

    bank = Bank()

    while True:
        show_menu()
        option = input("Select an option: ").strip()

        try:
            if option == "1":
                if issubclass(SavingsAccount, BankAccount):
                    holder = input("Enter account holder name: ").strip()
                    if not holder:
                        print("Error: Holder name cannot be empty.")
                        continue
                    balance = float(input("Enter initial balance: "))
                    account = SavingsAccount(holder, balance)
                    bank.add_account(account)
                    print(f"Account created successfully! Number: {account.number}")

            elif option == "2":
                if issubclass(CheckingAccount, BankAccount):
                    holder = input("Enter account holder name: ").strip()
                    if not holder:
                        print("Error: Holder name cannot be empty.")
                        continue
                    balance = float(input("Enter initial balance: "))
                    account = CheckingAccount(holder, balance)
                    bank.add_account(account)
                    print(f"Account created successfully! Number: {account.number}")

            elif option == "3":
                if issubclass(PremiumAccount, BankAccount):
                    holder = input("Enter account holder name: ").strip()
                    if not holder:
                        print("Error: Holder name cannot be empty.")
                        continue
                    balance = float(input("Enter initial balance: "))
                    account = PremiumAccount(holder, balance)
                    bank.add_account(account)
                    print(f"Account created successfully! Number: {account.number}")
                    account.show_benefits()

            elif option == "4":
                num = input("Enter account number: ").strip().upper()
                account = bank.find_account(num)
                if hasattr(account, "deposit"):
                    amount = float(input("Enter amount to deposit: "))
                    account.deposit(amount)
                    print(f"Deposit successful. New balance: ${account.balance:,.2f}")

            elif option == "5":
                num = input("Enter account number: ").strip().upper()
                account = bank.find_account(num)
                if hasattr(account, "withdraw"):
                    amount = float(input("Enter amount to withdraw: "))
                    account.withdraw(amount)
                    print(f"Withdrawal successful. New balance: ${account.balance:,.2f}")

            elif option == "6":
                origin = input("Enter origin account number: ").strip().upper()
                dest = input("Enter destination account number: ").strip().upper()
                amount = float(input("Enter amount to transfer: "))
                bank.transfer(origin, dest, amount)

            elif option == "7":
                num = input("Enter premium account number: ").strip().upper()
                account = bank.find_account(num)
                if hasattr(account, "history"):
                    print(f"\n--- Audit History for {num} ---")
                    for log in account.history:
                        print(log)
                elif hasattr(account, "generate_audit_report"):
                    print(f"\n--- Audit Report for {num} ---")
                    for line in account.generate_audit_report():
                        print(line)
                else:
                    print("This account type does not support auditing features.")

            elif option == "8":
                print("\n--- BALANCE RANKING ---")
                for acc in bank.get_balance_ranking():
                    print(f"{acc.number} - {acc.holder}: ${acc.balance:,.2f}")

            elif option == "9":
                print()
                for line in bank.generate_report():
                    print(line)

            elif option == "10":
                save(bank)
                export_summary(bank)
                print("Data saved successfully (JSON and Binary formats generated).")
                
            elif option == "11":
                loaded_accounts_data = load()
                if loaded_accounts_data:
                    bank._accounts.clear()
                    
                    for data in loaded_accounts_data:
                        cls_name = data.get("account_class")
                        holder = data.get("holder")
                        balance = data.get("balance")
                        
                        if cls_name == "SavingsAccount":
                            acc = SavingsAccount(holder, balance)
                        elif cls_name == "CheckingAccount":
                            acc = CheckingAccount(holder, balance)
                        elif cls_name == "PremiumAccount":
                            acc = PremiumAccount(holder, balance)
                        else:
                            continue
                            
                        acc._BankAccount__number = data.get("number")
                        bank.add_account(acc)
                        
                    print("Data loaded successfully into memory.")
                    import_summary() 
                else:
                    print("No saved data found or file is empty.")

            elif option == "0":
                print("Thank you for using Smart Bank. Goodbye!")
                break

            else:
                print("Invalid option. Please try again.")

        except ValueError:
            print("Error: Invalid numeric input. Please enter numbers only.")
        except BankError as e:
            print(f"Bank Error: {e}")
        except Exception as e:
            print(f"Unexpected System Error: {e}")

if __name__ == "__main__":
    main()
