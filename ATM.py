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

