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