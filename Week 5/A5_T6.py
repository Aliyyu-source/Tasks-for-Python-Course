# main.py

def showOptions():
    """Print available menu options."""
    print("Options:")
    print("1 - Show count")
    print("2 - Increase count")
    print("3 - Reset count")
    print("0 - Exit")


def askChoice():
    """
    Ask the user for a menu choice.
    Always returns an integer.
    If the input is not numeric, prints 'Unknown option!' and returns -1.
    """
    user_input = input("Your choice: ")

    # Check if the input is numeric, as in W3Schools isnumeric() example
    # https://www.w3schools.com/python/ref_string_isnumeric.asp
    if user_input.isnumeric():
        return int(user_input)
    else:
        print("Unknown option!")
        return -1  # special value for "invalid" input


def main():
    """Main program logic with menu loop."""
    print("Program starting.")

    count = 0
    running = True

    while running:
        showOptions()
        choice = askChoice()

        # Valid numeric options
        if choice == 1:
            print(f"Current count - {count}")
            print()  # blank line for readability
        elif choice == 2:
            count += 1
            print("Count increased!")
        elif choice == 3:
            count = 0
            print("Cleared count!")
        elif choice == 0:
            print("Exiting program.")
            running = False
        # Non-numeric or unknown numeric values
        elif choice != -1:
            # -1 already printed "Unknown option!" in askChoice
            print("Unknown option!")

    print()
    print("Program ending.")


if __name__ == "__main__":
    main()
