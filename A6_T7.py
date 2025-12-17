import os

LOWER = "abcdefghijklmnopqrstuvwxyz"
UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def rot13_char(ch: str) -> str:
    """Return ROT13 ciphered version of a single character."""
    if ch in LOWER:
        idx = LOWER.index(ch)
        return LOWER[(idx + 13) % 26]
    if ch in UPPER:
        idx = UPPER.index(ch)
        return UPPER[(idx + 13) % 26]
    return ch


def rot13_line(line: str) -> str:
    """Cipher/decipher a whole line using ROT13."""
    return "".join(rot13_char(c) for c in line)


def get_location_name(loc_id: int) -> str:
    """Map location id to place name."""
    names = {
        0: "home",
        1: "Galba's palace",
        2: "Otho's palace",
        3: "Vitellius' palace",
        4: "Vespasian's palace",
    }
    return names.get(loc_id, f"Unknown location ({loc_id})")


def read_progress(filename: str = "player_progress.txt") -> tuple[int, int, str]:
    """
    Read the latest progress from player_progress.txt.
    Returns (current_location, next_location, passphrase_ciphered).
    """
    if not os.path.exists(filename):
        raise FileNotFoundError(f'"{filename}" not found.')

    with open(filename, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    # Expect at least header + one data row
    if len(lines) < 2:
        raise ValueError("Progress file has no data rows.")

    # Use the last data row as current progress
    last = lines[-1]
    parts = last.split(";")
    if len(parts) != 3:
        raise ValueError("Invalid progress line format.")
    cur = int(parts[0])
    nxt = int(parts[1])
    cipher_pass = parts[2]
    return cur, nxt, cipher_pass


def append_progress_line(line: str, filename: str = "player_progress.txt") -> None:
    """Append a line to the progress file."""
    with open(filename, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def main() -> None:
    print("Travel starting.")

    # 1. Read progress (current location, next location, ciphered passphrase)
    current_loc, next_loc, passphrase_cipher = read_progress()
    current_name = get_location_name(current_loc)
    next_name = get_location_name(next_loc)

    print(f"Currently at {current_name}.")
    print(f"Travelling to {next_name}...")
    print(f"...Arriving to the {next_name}.")

    # 2. Decipher passphrase (ROT13) and "shout" it
    plain_passphrase = rot13_line(passphrase_cipher)
    print("Passing the guard at the entrance.")
    print(f"\"{plain_passphrase}!\"")

    # 3. Find and read the Emperor's ciphered message file
    #    File name format: "{NextLocationId}_{PassPhrase}.gkg"
    message_filename = f"{next_loc}_{passphrase_cipher}.gkg"
    print("Looking for the message in the palace...")

    if not os.path.exists(message_filename):
        print(f"Ah, there it is! Seems cryptic.")
        print(f"[Warning] Expected message file '{message_filename}' not found.")
        print("Time to leave...")
        print("Travel ending.")
        return

    print("Ah, there it is! Seems cryptic.")

    with open(message_filename, "r", encoding="utf-8") as f:
        message_lines_cipher = f.readlines()

    # 4. Save ciphered first line into player_progress.txt
    if message_lines_cipher:
        first_line_cipher = message_lines_cipher[0].rstrip("\n")
    else:
        first_line_cipher = ""

    # Append as a new progress line; here we keep the same current/next just
    # to demonstrate storing the message. You can change logic later to move on.
    progress_message_line = f"{current_loc};{next_loc};{first_line_cipher}"
    append_progress_line(progress_message_line)

    print("[Game] Progress autosaved!")

    # 5. Decipher full message and save plain version
    print("Deciphering Emperor's message...")
    plain_lines = [rot13_line(line.rstrip("\n")) for line in message_lines_cipher]

    # File name: "{NextLocationId}-{PlainPassPhrase}.txt"
    plain_message_filename = f"{next_loc}-{plain_passphrase}.txt"
    with open(plain_message_filename, "w", encoding="utf-8") as f:
        for line in plain_lines:
            f.write(line + "\n")

    print("Looks like I've got now the plain version copy of the Emperor's message.")
    print("Time to leave...")
    print("Travel ending.")


if __name__ == "__main__":
    main()

