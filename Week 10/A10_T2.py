########################################################
# Task A10_T2
# Developer Aliyyu Zen-Abdeen
# Date 2025-12-24
########################################################

import sys


def readValues(filename: str, values: list[int]) -> None:
    """Read integers from file into values list. Ignore empty lines."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                stripped = line.strip()
                if stripped == "":
                    continue  # skip empty lines[web:331][web:333][web:334]
                number = int(stripped)  # convert to int
                values.append(number)
    except Exception as e:
        print(f"Error reading file '{filename}': {e}")
        sys.exit(1)  # exit on error[web:336][web:268]


def sumOfValues(values: list[int]) -> int:
    """Return sum of all values."""
    total = 0
    for v in values:
        total += v  # manual sum so it is easy to understand[web:335][web:337]
    return total


def productOfValues(values: list[int]) -> int:
    """Return product of all values."""
    product = 1
    for v in values:
        product *= v
    return product


def main() -> None:
    # 1. Initialize
    values: list[int] = []

    # 2. Operate
    print("Program starting.")
    filename = input("Insert filename: ")

    # 2.2 read values
    readValues(filename, values)

    # 2.3 calculate sum
    total_sum = sumOfValues(values)

    # 2.4 calculate product
    total_product = productOfValues(values)

    # 2.5 display results
    print("# --- Sum of numbers --- #")
    print(total_sum)
    print("# --- Sum of numbers --- #")
    print("# --- Product of numbers --- #")
    print(total_product)
    print("# --- Product of numbers --- #")

    # 3. Cleanup
    values.clear()
    print("Program ending.")


if __name__ == "__main__":
    main()
