########################################################
# Task A10_T6
# Developer Aliyyu Zen-Abdeen
# Date 2025-12-24
########################################################

import copy
import time
from typing import Callable


def readValues(PValues: list[int]) -> str:
    """Ask filename, read ints into PValues, return filename."""
    PValues.clear()
    filename = input("Insert dataset filename: ")
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            stripped = line.strip()
            if stripped == "":
                continue
            PValues.append(int(stripped))
    return filename


def bubbleSort(PNums: list[int]) -> list[int]:
    """In-place bubble sort, ascending order."""
    n = len(PNums)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if PNums[j] > PNums[j + 1]:  # ascending[web:338][web:340]
                PNums[j], PNums[j + 1] = PNums[j + 1], PNums[j]
                swapped = True
        if not swapped:
            break
    return PNums


def _partition(PNums: list[int], low: int, high: int) -> int:
    """Partition helper for quick sort (Lomuto-style)."""
    pivot = PNums[high]
    i = low - 1
    for j in range(low, high):
        if PNums[j] <= pivot:
            i += 1
            PNums[i], PNums[j] = PNums[j], PNums[i]
    PNums[i + 1], PNums[high] = PNums[high], PNums[i + 1]
    return i + 1


def _quickSort_recursive(PNums: list[int], low: int, high: int) -> None:
    if low < high:
        p = _partition(PNums, low, high)  # standard quicksort pattern[web:365][web:368]
        _quickSort_recursive(PNums, low, p - 1)
        _quickSort_recursive(PNums, p + 1, high)


def quickSort(PNums: list[int]) -> list[int]:
    """In-place quick sort, ascending order."""
    if len(PNums) > 1:
        _quickSort_recursive(PNums, 0, len(PNums) - 1)
    return PNums


def measureSortingTime(PSortingAlgorithm: Callable, PArr: list[int]) -> int:
    """Measure elapsed time in nanoseconds for given sorting function."""
    start_time = time.perf_counter_ns()  # high-resolution timer[web:370][web:372]
    PSortingAlgorithm(PArr)
    end_time = time.perf_counter_ns()
    elapsed = end_time - start_time
    return elapsed


def print_menu() -> None:
    print("Options:")
    print("1 - Read dataset values")
    print("2 - Measure speeds")
    print("3 - Save results")
    print("0 - Exit")


def main() -> None:
    # 1. Initialize
    Values: list[int] = []
    Results: list[str] = []
    current_dataset_name: str | None = None

    # 2. Operate
    print("Program starting.")

    while True:
        print()
        print_menu()
        choice = input("Your choice: ").strip()

        if choice == "1":
            current_dataset_name = readValues(Values)
        elif choice == "2":
            if not Values:
                print("No dataset loaded. Please choose option 1 first.")
                continue
            if current_dataset_name is None:
                current_dataset_name = "Unknown"

            builtin_time = measureSortingTime(sorted, copy.deepcopy(Values))
            bubble_time = measureSortingTime(bubbleSort, copy.deepcopy(Values))
            quick_time = measureSortingTime(quickSort, copy.deepcopy(Values))

            line1 = f"Measured speeds for dataset '{current_dataset_name}':"
            line2 = f" - Built-in sorted {builtin_time} ns"
            line3 = f" - Buble sort {bubble_time} ns"
            line4 = f" - Quick sort {quick_time} ns"

            print(line1)
            print(line2)
            print(line3)
            print(line4)

            # store full block into Results for later saving
            Results.append(line1)
            Results.append(line2)
            Results.append(line3)
            Results.append(line4)
            Results.append("")  # empty line between datasets
        elif choice == "3":
            if not Results:
                print("No results to save. Measure speeds first.")
                continue
            out_name = input("Insert results filename: ")
            with open(out_name, "w", encoding="utf-8") as f:
                for line in Results:
                    f.write(line + "\n")
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please select 0, 1, 2 or 3.")

    # 3. Cleanup
    Values.clear()
    Results.clear()
    print("Program ending.")


if __name__ == "__main__":
    main()
