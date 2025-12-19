from calc_lib import add, subtract, multiply, divide


def showOptions() -> None:
    print("Options:")
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")
    print("0 - Exit")


def askChoice() -> int:
    choice_str = input("Your choice: ")
    try:
        return int(choice_str)
    except ValueError:
        return -1  # invalid


def askValue(PPrompt: str) -> float:
    value_str = input(PPrompt)
    return float(value_str)


def main() -> None:
    print("Program starting.")

    while True:
        showOptions()
        choice = askChoice()

        if choice == 0:
            print("Exiting program.\n")
            break

        elif choice == 1:
            a = askValue("Insert first addend value: ")
            b = askValue("Insert second addend value: ")
            result = add(a, b)
            print(f"{a} + {b} = {result}\n")

        elif choice == 2:
            a = askValue("Insert minuend value: ")
            b = askValue("Insert subtrahend value: ")
            result = subtract(a, b)
            print(f"{a} - {b} = {result}\n")

        elif choice == 3:
            a = askValue("Insert multiplicant value: ")
            b = askValue("Insert multiplier value: ")
            result = multiply(a, b)
            print(f"{a} * {b} = {result}\n")

        elif choice == 4:
            a = askValue("Insert dividend value: ")
            b = askValue("Insert divisor value: ")
            result = divide(a, b)
            print(f"{a} / {b} = {result}\n")

        else:
            print("Invalid choice.\n")

    print("Program ending.")


if __name__ == "__main__":
    main()
