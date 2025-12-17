SEPARATOR = ";"


def readValues(filename: str) -> str:
    """
    Read integer values from a text file.
    Returns a single string with numbers separated by SEPARATOR.
    """
    values = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            num_str = line.strip()
            if num_str:
                values.append(num_str)
    return SEPARATOR + SEPARATOR.join(values) + SEPARATOR  # optional framing


def analyseNumbers(values_str: str) -> tuple[int, int, int, float]:
    """
    Analyse the numbers stored in a SEPARATOR-separated string.
    Returns (count, total_sum, greatest, average).
    """
    # Remove possible leading/trailing separators and split
    parts = [p for p in values_str.split(SEPARATOR) if p != ""]
    nums = [int(p) for p in parts]

    count = len(nums)
    if count == 0:
        return 0, 0, 0, 0.0

    total_sum = sum(nums)
    greatest = max(nums)
    average = total_sum / count
    return count, total_sum, greatest, average


def printResults(filename: str, count: int, total_sum: int, greatest: int, average: float) -> None:
    """
    Print the results in the requested CSV-style format.
    """
    print("#### Number analysis - START ####")
    print(f'File "{filename}" results:')
    print("Count;Sum;Greatest;Average")
    print(f"{count};{total_sum};{greatest};{average:.2f}")
    print()
    print("#### Number analysis - END ####")


def main() -> None:
    print("Program starting.")
    filename = input("Insert filename: ")

    values_str = readValues(filename)
    count, total_sum, greatest, average = analyseNumbers(values_str)
    printResults(filename, count, total_sum, greatest, average)

    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
