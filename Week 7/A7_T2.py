def main() -> None:
    print("Program starting.")
    raw = input("Insert comma separated integers: ")

    parts = raw.split(",")
    valid_numbers: list[int] = []

    for part in parts:
        s = part.strip()
        if s == "":
            continue
        if s.lstrip("-").isdigit():
            valid_numbers.append(int(s))
        else:
            print(f'Invalid value: "{s}"')

    if not valid_numbers:
        print("No valid integers to analyse.")
        print("Program ending.")
        return

    count = len(valid_numbers)
    total = sum(valid_numbers)

    print(f"There are {count} integers in the list.")
    if total % 2 == 0:
        parity = "even"
    else:
        parity = "odd"
    print(f"Sum of the integers is {total} and it's {parity}")
    print("Program ending.")


if __name__ == "__main__":
    main()
