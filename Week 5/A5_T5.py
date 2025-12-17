def showOptions():
    """Print the menu options."""
    print("Options:")
    print("1 - Insert word")
    print("2 - Show current word")
    print("3 - Show current word in reverse")
    print("0 - Exit")


def main():
    """Main function running the menu-driven program."""
    print("Program starting.")

    word = ""        # stored word starts empty
    running = True

    while running:
        showOptions()
        choice = input("Your choice: ")

        print()  # empty line after choice section

        if choice == "1":
            word = input("Insert word: ")
            print()
        elif choice == "2":
            print(f'Current word - "{word}"')
            print()
        elif choice == "3":
            reversed_word = word[::-1]
            print(f'Word reversed - "{reversed_word}"')
            print()
        elif choice == "0":
            print("Exiting program.")
            print()
            running = False
        else:
            print("Unknown option!")
            print()

    print("Program ending.")


if __name__ == "__main__":
    main()
