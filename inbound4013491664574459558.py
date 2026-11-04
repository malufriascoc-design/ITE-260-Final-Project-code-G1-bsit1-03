CURRENCY = "PHP"    
LINE = "=" * 60
WARNING_LIMIT = 80   


def show_menu():
    print(LINE)
    print("  STUDENT EXPENSE TRACKER")
    print(LINE)
    print("  [1] Record Allowance")
    print("  [2] Record Expense")
    print("  [3] View Transaction History")
    print("  [4] View Balance and Budget Status")
    print("  [5] View Full Summary Report")
    print("  [0] Exit")
    print(LINE)


def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            record_allowance()
        elif choice == "2":
            record_expense()
        elif choice == "3":
            view_history()
        elif choice == "4":
            view_budget_status()
        elif choice == "5":
            view_full_summary()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


def record_allowance():
    print("\n--- Record Allowance ---")
    print("(SOURCE EXAMPLE: allowance, School Assistance)")
    source = read_text("SOURCE  : ")
    amount = read_amount("AMOUNT  : ")
    allowance_records.append([source, amount])

    print(f"Recorded : {CURRENCY} {amount:.2f}")
    print(f"Total allowance: {CURRENCY} {total_allowance():.2f}")


def record_expense():
    print("--- Record Expense ---")

    if not allowance_records:
        print("No allowance recorded yet. Record it first.")
        return

    print(f"Current balance : {CURRENCY} {balance():.2f}")

    print("Select a category:")
    print("  1. Food")
    print("  2. Transportation")
    print("  3. Purchases")

    choice = input("Category number: ").strip()

    if choice == "1":
        category = "Food"
    elif choice == "2":
        category = "Transportation"
    elif choice == "3":
        category = "Purchases"
    else:
        print("Invalid category.")
        return

    description = read_text("Description: ")
    amount = read_amount(f"Amount spent : ")

    if amount > balance():
        print(f"This is more than your remaining balance of {CURRENCY} {balance():.2f}.")
        answer = input("Record it anyway? (y/n): ").strip().lower()

        if answer != "y":
            print("Expense cancelled.")
            return

    expense_records.append([category, description, amount])

    print(f"Recorded {category} expense of : {CURRENCY} {amount:.2f}.")
    print(f"Remaining balance : {CURRENCY} {balance():.2f}")

    if total_allowance() > 0:
        percent_used = total_expenses() / total_allowance() * 100

        if percent_used >= WARNING_LIMIT:
            print(f"Warning: {percent_used:.1f}% of your allowance is used.")


allowance_records = []
expense_records = []
 

def view_history():
    print("\n--- Transaction History ---")

    print("\nAllowance:")
    if len(allowance_records) == 0:
        print("  None recorded yet.")
    else:
        for source, amount in allowance_records:
            print(f"  {source}: {CURRENCY} {amount:.2f}")
        print(f"  Total: {CURRENCY} {total_allowance():.2f}")

    print("\nExpenses:")
    if len(expense_records) == 0:
        print("  None recorded yet.")
    else:
        for category, description, amount in expense_records:
            print(f"  [{category}] {description}: {CURRENCY} {amount:.2f}")
        print(f"  Total: {CURRENCY} {total_expenses():.2f}")


def read_amount(prompt):
    while True:
        text = input(prompt).strip()
        try:
            amount = float(text)
        except ValueError:
            print("Please enter a valid number, like 150 or 75.50.")
            continue
        if amount <= 0:
            print("Amount must be greater than 0.")
            continue
        return round(amount, 2)


def read_text(prompt):
    while True:
        text = input(prompt).strip()
        if text != "":
            return text
        print("This field cannot be empty.")


def total_allowance():
    total = 0
    for record in allowance_records:
        total += record[1]
    return total


def total_expenses():
    total = 0
    for record in expense_records:
        total += record[2]
    return total


def balance():
    return total_allowance() - total_expenses()


def view_budget_status():
    print(LINE)
    print("\n--- BALANCE AND BUDGET STATUS ---")
    print(f"  Total Allowance : {CURRENCY} {total_allowance():.2f}")
    print(f"  Total Expenses  : {CURRENCY} {total_expenses():.2f}")
    print(f"  Balance         : {CURRENCY} {balance():.2f}")

    if total_allowance() == 0:
        print("  Record your allowance first.")
        return

    percent_used = total_expenses() / total_allowance() * 100
    print(f"  Budget Used: {percent_used:.1f}%")

    if balance() < 0:
        print(f"  Over budget by {CURRENCY} {abs(balance()):.2f}.")
    elif percent_used >= WARNING_LIMIT:
        print("  Warning: getting close to your limit.")
    else:
        print("  On track.")


def view_full_summary():
    print("\n" + LINE)
    print("  FULL SUMMARY REPORT")
    print(LINE)
    print(f"  Allowance entries : {len(allowance_records)}")
    print(f"  Expense entries   : {len(expense_records)}")
    view_budget_status()


main()
