def print_menu() -> None:
    print("Options:")
    print("1 - Read values")
    print("2 - Amount of values")
    print("3 - Calculate sum of values")
    print("4 - Calculate average of values")
    print("0 - Exit")


def read_values() -> list[float]:
    filename = input("Insert filename: ")
    values: list[float] = []

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            row = line.strip()
            if row == "":
                continue
            values.append(float(row))

    print()
    return values


def calc_sum(values: list[float]) -> float:
    return sum(values)


def calc_average(values: list[float]) -> float:
    if len(values) == 0:
        return 0.0
    return sum(values) / len(values)


def main() -> None:
    print("Program starting.")
    values: list[float] = []

    while True:
        print_menu()
        choice = input("Your choice: ")

        if choice == "1":
            values = read_values()

        elif choice == "2":
            print(f"Amount of values {len(values)}\n")

        elif choice == "3":
            total = calc_sum(values)
            print(f"Sum of values {round(total, 1)}\n")

        elif choice == "4":
            avg = calc_average(values)
            print(f"Average of values {round(avg, 1)}\n")

        elif choice == "0":
            print("Exiting program.\n")
            break

        else:
            print("Invalid choice.\n")

    print("Program ending.")


if __name__ == "__main__":
    main()
