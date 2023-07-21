# Define the login function that takes in the correct PIN as a parameter
def login(correct_pin):
    attempts = 3

    # Loop until the user runs out of attempts
    while attempts > 0:
        pin = int(input("Enter your PIN: "))

        # Check if the entered PIN matches the correct PIN
        if pin == correct_pin:
            print("Login successful!")
            return True
        else:
            attempts -= 1
            print(f"Incorrect PIN. Attempts left: {attempts}")
            print()

    # Print a message if the user runs out of attempts
    print("=" * 80)
    print("\033[33mToo many incorrect attempts. Exiting...\033[0m")
    return False


# Function to check the account balance
def check_balance(balance):
    print(f"Your current balance is: ${balance}") 


# Function to deposit money into the account
def deposit(balance):
    amount = float(input("Enter the amount to deposit: $"))

    # Check if the amount is valid (greater than 0)
    if amount > 0:
        balance += amount
        print(f"Deposit successful. Your new balance is: ${balance}")
        return balance
    else:
        print("Invalid amount. Deposit failed.")


# Function to withdraw money from the account
def withdraw(balance):
    amount = float(input("Enter the amount to withdraw: $"))

    # Check if the amount is valid (greater than 0) and if there are sufficient funds
    if amount > 0 and amount <= balance:
        balance -= amount
        print(f"Withdrawal successful. Your new balance is: ${balance}")
        return balance
    else:
        print("Insufficient funds or invalid amount. Withdrawal failed.")


# Print the welcome message and the ATM ASCII art
print("=" * 80)
print(
    "       ========= \033[32m __  \033[0m========\033[32m _________ \033[0m========\033[32m __    __ \033[0m========")
print(
    "       ========= \033[32m/  \ \033[0m========\033[32m|___   ___|\033[0m========\033[32m|  \  /  |\033[0m========")
print(
    "       ======== \033[32m/ /\ \ \033[0m===========\033[32m| |\033[0m============\033[32m|   \/   |\033[0m========")
print(
    "       ======= \033[32m/ ____ \ \033[0m==========\033[32m| |\033[0m============\033[32m| |\__/| |\033[0m========")
print("       ====== \033[32m/ /\033[0m====\033[32m\ \ \033[0m=========\033[32m| |\033[0m============\033[32m| |\033[0m====\033[32m| |\033[0m========")
print("       ===== \033[32m/_/\033[0m======\033[32m\_\ \033[0m========\033[32m|_|\033[0m============\033[32m|_|\033[0m====\033[32m|_|\033[0m========")
print("=" * 80)

print("\t\t\t\033[33mWELCOME TO OUR ATM SERVICE\033[0m")
print("=" * 80)

# Define the list of user information
users = [
    {"userName": "John", "pin": 2021, "balance": 500},
    {"userName": "Jane", "pin": 1920, "balance": 1050},
    {"userName": "Mike", "pin": 2122, "balance": 3500}
]

selected_user = None
name = str(input("Enter your username: "))
