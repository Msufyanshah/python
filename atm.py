class ATM:
    def __init__(self):
        self.balance = 5000
        self.pin = 1234
        self.is_authenticated = False

    def check_pin(self, input_pin):
        if input_pin == self.pin:
            self.is_authenticated = True
            print("✅ PIN is correct. Access granted.")
        else:
            self.is_authenticated = False
            print("❌ Incorrect PIN. Access denied.")

    def check_balance(self):
        if self.is_authenticated:
            print(f"💰 Your current balance is: Rs. {self.balance}")
        else:
            print("🔐 Please enter correct PIN first.")

    def deposit(self, amount):
        if not self.is_authenticated:
            print("🔐 Please enter correct PIN first.")
            return
        if amount <= 0:
            print("❌ Deposit amount must be positive.")
        else:
            self.balance += amount
            print(f"✅ Rs. {amount} deposited successfully.")
            self.check_balance()

    def withdraw(self, amount):
        if not self.is_authenticated:
            print("🔐 Please enter correct PIN first.")
            return
        if amount <= 0:
            print("❌ Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("❌ Insufficient balance.")
        else:
            self.balance -= amount
            print(f"✅ Rs. {amount} withdrawn successfully.")
            self.check_balance()

    def exit(self):
        print("👋 Thank you for using the ATM. Goodbye!")
        quit()


# --------------------------
# ATM User Interface (CLI)
# --------------------------

atm = ATM()

while True:
    print("\n====== ATM Menu ======")
    print("1. Enter PIN")
    print("2. Check Balance")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Exit")
    choice = input("Select an option (1-5): ")

    if choice == "1":
        try:
            pin_input = int(input("Enter your 4-digit PIN: "))
            atm.check_pin(pin_input)
        except ValueError:
            print("❌ Invalid input. PIN must be a number.")

    elif choice == "2":
        atm.check_balance()

    elif choice == "3":
        try:
            amount = float(input("Enter deposit amount: "))
            atm.deposit(amount)
        except ValueError:
            print("❌ Invalid amount. Please enter a number.")

    elif choice == "4":
        try:
            amount = float(input("Enter withdrawal amount: "))
            atm.withdraw(amount)
        except ValueError:
            print("❌ Invalid amount. Please enter a number.")

    elif choice == "5":
        atm.exit()

    else:
        print("❌ Invalid choice. Please select from the menu.")
