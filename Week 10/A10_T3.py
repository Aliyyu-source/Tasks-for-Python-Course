########################################################
# Task A10_T3
# Developer Aliyyu Zen-Abdeen
# Date 2025-12-24
########################################################

import sys


def read_values(filename: str) -> list[int]:
    """Read integers from file, ignore empty lines."""
    values: list[int] = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            stripped = line.strip()
            if stripped == "":
                continue  # skip empty rows[web:331]
            values.append(int(stripped))
    return values


def bubbleSort(PValues: list[int], PAsc: bool = True) -> None:
    """In-place bubble sort. Sort ascending by default, descending if PAsc is False."""
    n = len(PValues)
    # Standard bubble sort with early exit optimization[web:338][web:340]
    for i in range(n):
        swapped = False
        # Remaining = n - i - 1
        for j in range(0, n - i - 1):
            if PAsc:
                condition = PValues[j] > PValues[j + 1]
            else:
                condition = PValues[j] < PValues[j + 1]

            if condition:
                PValues[j], PValues[j + 1] = PValues[j + 1], PValues[j]
                swapped = True

        if not swapped:
            break  # already sorted, stop early


def values_to_str(values: list[int]) -> str:
    """Convert list of ints to 'a, b, c' string."""
    return ", ".join(str(v) for v in values)


def get_filename_from_cli_or_input() -> str:
    """If one CLI arg given, use it; otherwise ask user."""
    if len(sys.argv) == 2:  # script name + 1 argument[web:305][web:344]
        return sys.argv[1]
    return input("Insert filename: ")


def main() -> None:
    print("Program starting.")
    filename = get_filename_from_cli_or_input()

    values_raw = read_values(filename)

    # Raw
    print(f"Raw '{filename}' -> {values_to_str(values_raw)}")

    # Ascending
    values_asc = values_raw.copy()
    bubbleSort(values_asc, True)
    print(f"Ascending '{filename}' -> {values_to_str(values_asc)}")

    # Descending
    values_desc = values_raw.copy()
    bubbleSort(values_desc, False)
    print(f"Descending '{filename}' -> {values_to_str(values_desc)}")

    print("Program ending.")


if __name__ == "__main__":
    main()
