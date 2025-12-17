def askName():
    """Prompt the user to insert a name and return it."""
    name = input("Insert name: ")
    return name


def greetUser(PName):
    """Greet the user by the given name."""
    print(f"Hello {PName}!")
    return None


def main():
    """Main function: coordinates the program flow."""
    print("Program starting.")
    user_name = askName()
    greetUser(user_name)
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
