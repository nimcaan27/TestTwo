try:
    # Try to convert a user input to an integer
    user_input = input("Enter a number: ")
    number = int(user_input)
    print(f"The number you entered is: {number}")
except ValueError:
    # This block handles the case where the input is not a valid integer
    print("Oops! That's not a valid number. Please enter a valid integer.")
