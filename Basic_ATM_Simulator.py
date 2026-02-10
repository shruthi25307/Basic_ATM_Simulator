account_balance = 5000
while True:
 print("\n===== Welcome to Your ATM =====")
 print("1. View Balance")
 print("2. Add Money")
 print("3. Withdraw Money")
 print("4. Exit")
 user_choice = int(input("Select an option: "))
 if user_choice == 1:
 print("Current Balance: Rs.", account_balance)
 elif user_choice == 2:
 deposit_amount = float(input("Enter amount to deposit: "))
 account_balance += deposit_amount
 print("Deposit successful!")
 elif user_choice == 3:
 withdraw_amount = float(input("Enter amount to withdraw: "))
 if withdraw_amount <= account_balance:
 account_balance -= withdraw_amount
 print("Please collect your cash")
 else:
 print("Not enough balance")
 elif user_choice == 4:
 print("Exiting ATM. Have a nice day!")
 break
 else:
 print("Invalid option, please try again")
