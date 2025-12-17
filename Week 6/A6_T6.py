LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def rot13_char(ch: str) -> str:
    """Return ROT13 ciphered version of a single character."""
    if ch in LOWER_ALPHABETS:
        idx = LOWER_ALPHABETS.index(ch)
        return LOWER_ALPHABETS[(idx + 13) % 26]
    elif ch in UPPER_ALPHABETS:
        idx = UPPER_ALPHABETS.index(ch)
        return UPPER_ALPHABETS[(idx + 13) % 26]
    else:
        return ch  # non-letters stay the same


def rot13_line(line: str) -> str:
    """Cipher a whole line using ROT13."""
    result = []
    for ch in line:
        result.append(rot13_char(ch))
    return "".join(result)


def collect_plaintext() -> list[str]:
    """Collect plain text rows until an empty row is inserted."""
    print("Collecting plain text rows for ciphering.")
    lines = []
    while True:
        row = input("Insert row(empty stops): ")
        if row == "":
            break
        lines.append(row)
    return lines


def save_ciphered(lines: list[str]) -> None:
    """Ask filename and save ciphered lines into a file."""
    filename = input("Insert filename to save: ")
    with open(filename, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")
    print("Ciphered text saved!")


def main() -> None:
    print("Program starting.")
    print()

    # 1. Collect plain text
    plain_lines = collect_plaintext()

    # 2. Cipher all lines
    cipher_lines = [rot13_line(line) for line in plain_lines]

    # 3. Ask user what to do with ciphered text
    print()
    choice = input("Show ciphered text on screen (S) or save to file (F)? ").strip().upper()

    print()
    if choice == "S":
        print("#### Ciphered text ####")
        for line in cipher_lines:
            print(line)
        print()
        print("#### Ciphered text ####")
    elif choice == "F":
        print("#### Ciphered text ####")
        for line in cipher_lines:
            print(line)
        print()
        print("#### Ciphered text ####")
        save_ciphered(cipher_lines)
    else:
        print("Unknown option! Showing ciphered text by default.")
        print("#### Ciphered text ####")
        for line in cipher_lines:
            print(line)
        print()
        print("#### Ciphered text ####")

    print("Program ending.")


if __name__ == "__main__":
    main()
