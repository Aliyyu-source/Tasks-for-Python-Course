########################################################
# Task A10_T1
# Developer Aliyyu Zen-Abdeen
# Date 2025-12-24
########################################################

def read_values(filename: str) -> list[str]:
    """Read non-empty lines from file, strip newlines, return as list."""
    values: list[str] = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            stripped = line.strip()          # remove newline and spaces[web:315]
            if stripped != "":              # ignore empty rows[web:312][web:318]
                values.append(stripped)
    return values


def print_vertically(values: list[str]) -> None:
    print("# --- Vertically --- #")
    for v in values:
        print(v)
    print("# --- Vertically --- #")


def print_horizontally(values: list[str]) -> None:
    print("# --- Horizontally --- #")
    # join with comma + space ", "[web:316][web:319]
    line = ", ".join(values)
    print(line)
    print("# --- Horizontally --- #")


def main() -> None:
    print("Program starting.")
    filename = input("Insert filename: ")
    values = read_values(filename)
    print_vertically(values)
    print_horizontally(values)
    print("Program ending.")


if __name__ == "__main__":
    main()
