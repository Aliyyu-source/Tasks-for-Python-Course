from datetime import datetime

MONTHS = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
)

WEEKDAYS = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
)


def read_timestamps(filename: str) -> list[datetime]:
    timestamps: list[datetime] = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            row = line.strip()
            if row == "":
                continue
            dt = datetime.strptime(row, "%Y-%m-%dT%H:%M")
            timestamps.append(dt)
    return timestamps


def calculate_years(year: int, timestamps: list[datetime]) -> int:
    count = 0
    for ts in timestamps:
        if ts.year == year:
            count += 1
    return count


def calculate_months(month_name: str, timestamps: list[datetime]) -> int:
    if month_name not in MONTHS:
        return 0
    month_index = MONTHS.index(month_name) + 1  # 1–12

    count = 0
    for ts in timestamps:
        if ts.month == month_index:
            count += 1
    return count


def calculate_weekdays(weekday_name: str, timestamps: list[datetime]) -> int:
    if weekday_name not in WEEKDAYS:
        return 0
    weekday_index = WEEKDAYS.index(weekday_name)  # Monday = 0, ..., Sunday = 6

    count = 0
    for ts in timestamps:
        if ts.weekday() == weekday_index:
            count += 1
    return count


def print_menu() -> None:
    print("Options:")
    print("1 - Calculate amount of timestamps during year")
    print("2 - Calculate amount of timestamps during month")
    print("3 - Calculate amount of timestamps during weekday")
    print("0 - Exit")


def main() -> None:
    print("Program starting.")
    filename = input("Insert filename: ")
    timestamps = read_timestamps(filename)

    while True:
        print_menu()
        choice = input("Your choice: ")

        if choice == "1":
            year_str = input("Insert year: ")
            year = int(year_str)
            count = calculate_years(year, timestamps)
            print(f"Amount of timestamps during year '{year}' is {count}\n")

        elif choice == "2":
            month = input("Insert month: ")
            count = calculate_months(month, timestamps)
            print(f"Amount of timestamps during month '{month}' is {count}\n")

        elif choice == "3":
            weekday = input("Insert weekday: ")
            count = calculate_weekdays(weekday, timestamps)
            print(f"Amount of timestamps during weekday '{weekday}' is {count}\n")

        elif choice == "0":
            print("Exiting program.\n")
            break

        else:
            print("Invalid choice.\n")

    print("Program ending.")


if __name__ == "__main__":
    main()
