def read_names_from_file(filename: str) -> list[str]:
    """
    Read names from the given file.
    Returns a list of non-empty, stripped name strings.
    """
    names = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            name = line.strip()
            if name:  # skip empty lines
                names.append(name)
    return names


def analyse_names(names: list[str]) -> tuple[int, int, int, float]:
    """
    Analyse the names list and return:
    (count, shortest_len, longest_len, average_len)
    If there are no names, all values are zero.
    """
    if not names:
        return 0, 0, 0, 0.0

    lengths = [len(n) for n in names]
    count = len(lengths)
    shortest = min(lengths)
    longest = max(lengths)
    avg = sum(lengths) / count
    return count, shortest, longest, avg


def main() -> None:
    print("Program starting.")
    print("This program analyses a list of names from a file.")

    filename = input("Insert filename to read: ")

    print(f'Reading names from "{filename}".')
    names = read_names_from_file(filename)

    print("Analysing names...")
    count, shortest, longest, avg = analyse_names(names)
    print("Analysis complete!")

    print("#### REPORT BEGIN ####")
    print(f"Name count - {count}")
    print(f"Shortest name - {shortest} chars")
    print(f"Longest name - {longest} chars")
    print("Average name - {:.2f} chars".format(avg))
    print("#### REPORT END ####")

    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
