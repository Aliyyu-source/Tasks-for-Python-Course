########################################################
# Task A10_T4
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
                continue
            values.append(int(stripped))  # convert to int[web:314][web:330]
    return values


def merge(PLeft: list[int], PRight: list[int], PMerge: list[int], PAsc: bool = True) -> None:
    """Merge two sorted lists PLeft and PRight into PMerge (ascending or descending)."""
    i = 0  # index for PLeft
    j = 0  # index for PRight
    k = 0  # index for PMerge

    # merge while both lists have elements[web:352][web:348]
    while i < len(PLeft) and j < len(PRight):
        if PAsc:
            condition = PLeft[i] <= PRight[j]
        else:
            condition = PLeft[i] >= PRight[j]
        if condition:
            PMerge[k] = PLeft[i]
            i += 1
        else:
            PMerge[k] = PRight[j]
            j += 1
        k += 1

    # copy remaining from PLeft
    while i < len(PLeft):
        PMerge[k] = PLeft[i]
        i += 1
        k += 1

    # copy remaining from PRight
    while j < len(PRight):
        PMerge[k] = PRight[j]
        j += 1
        k += 1


def mergeSort(PValues: list[int], PAsc: bool = True) -> None:
    """In-place wrapper-style merge sort: sorts PValues using extra lists."""
    n = len(PValues)
    if n <= 1:
        return

    mid = n // 2
    left = PValues[:mid]
    right = PValues[mid:]

    mergeSort(left, PAsc)
    mergeSort(right, PAsc)

    # PMerge is the original list; merge back into it
    merge(left, right, PValues, PAsc)  # modifies PValues in-place[web:348][web:352]


def values_to_str(values: list[int]) -> str:
    return ", ".join(str(v) for v in values)


def get_filename_from_cli_or_input() -> str:
    if len(sys.argv) == 2:  # script + 1 argument[web:351][web:354]
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
    mergeSort(values_asc, True)
    print(f"Ascending '{filename}' -> {values_to_str(values_asc)}")

    # Descending
    values_desc = values_raw.copy()
    mergeSort(values_desc, False)
    print(f"Descending '{filename}' -> {values_to_str(values_desc)}")

    print("Program ending.")


if __name__ == "__main__":
    main()
