WEEKDAYS = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturnday",
    "Sunday",
)


def readFile(PFilename: str, PRows: list[str]) -> None:
    print('Reading file "{}".'.format(PFilename))

    PRows.clear()

    with open(PFilename, "r", encoding="utf-8") as f:
        first = True
        for line in f:
            if first:
                first = False  # skip header row
                continue
            if line == "\n":
                continue
            PRows.append(line.rstrip("\n"))

    return None


def analyseTimestamps(PRows: list[str], PResults: list[str]) -> None:
    print("Analysing timestamps.")

    # helper list for weekday counts
    weekday_counts: list[int] = [0, 0, 0, 0, 0, 0, 0]

    for row in PRows:
        for j, wd in enumerate(WEEKDAYS):
            if row.startswith(wd + ";"):
                weekday_counts[j] += 1
                break

    PResults.append("### Timestamp analysis ###")
    for i, wd in enumerate(WEEKDAYS):
        PResults.append(f" - {wd} {weekday_counts[i]} stamps")
    PResults.append("### Timestamp analysis ###")

    weekday_counts.clear()
    return None


def displayResults(PResults: list[str]) -> None:
    print("Displaying results.")
    for line in PResults:
        print(line)
    return None


def main() -> None:
    print("Program starting.")

    rows: list[str] = []
    results: list[str] = []

    filename = input("Insert filename: ")

    readFile(filename, rows)
    analyseTimestamps(rows, results)
    displayResults(results)

    rows.clear()
    results.clear()

    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
