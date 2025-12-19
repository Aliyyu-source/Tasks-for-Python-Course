ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def load_config(filename: str):
    rotor1 = ""
    rotor2 = ""
    rotor3 = ""
    reflector = ""

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue
            if line.startswith("Rotor1:"):
                rotor1 = line.split(":", 1)[1].strip()
            elif line.startswith("Rotor2:"):
                rotor2 = line.split(":", 1)[1].strip()
            elif line.startswith("Rotor3:"):
                rotor3 = line.split(":", 1)[1].strip()
            elif line.startswith("Reflector:"):
                reflector = line.split(":", 1)[1].strip()

    return rotor1, rotor2, rotor3, reflector


def step_rotors(positions: list[int]) -> None:
    # simple stepping: always advance rotor1 by 1 (0–25),
    # and when it wraps, advance rotor2, etc.
    positions[0] = (positions[0] + 1) % 26
    if positions[0] == 0:
        positions[1] = (positions[1] + 1) % 26
        if positions[1] == 0:
            positions[2] = (positions[2] + 1) % 26


def forward_pass(letter: str, rotors: list[str], positions: list[int]) -> str:
    # go through rotor1 -> rotor2 -> rotor3
    idx = ALPHABET.index(letter)

    for i in range(3):
        pos = positions[i]
        # offset index
        shifted_index = (idx + pos) % 26
        # get mapped letter from rotor
        mapped_letter = rotors[i][shifted_index]
        # convert mapped letter back to base index for next rotor
        idx = ALPHABET.index(mapped_letter)

    return ALPHABET[idx]


def reflector_pass(letter: str, reflector: str) -> str:
    idx = ALPHABET.index(letter)
    return reflector[idx]


def reverse_pass(letter: str, rotors: list[str], positions: list[int]) -> str:
    # go back rotor3 -> rotor2 -> rotor1
    idx = ALPHABET.index(letter)

    for i in range(2, -1, -1):
        pos = positions[i]
        # rotor wiring at this rotor
        wiring = rotors[i]
        # we need to find which input index goes to our current letter index
        # reverse: find k such that wiring[(k + pos) % 26] == ALPHABET[idx]
        target_letter = ALPHABET[idx]
        for k in range(26):
            shifted_index = (k + pos) % 26
            if wiring[shifted_index] == target_letter:
                idx = k
                break

    return ALPHABET[idx]


def scramble_char(ch: str, rotors: list[str], reflector: str, positions: list[int]) -> str:
    if ch not in ALPHABET:
        return ch

    # step rotors BEFORE scrambling this char
    step_rotors(positions)

    # forward through rotors
    after_forward = forward_pass(ch, rotors, positions)

    # reflector
    after_reflector = reflector_pass(after_forward, reflector)

    # reverse through rotors
    after_reverse = reverse_pass(after_reflector, rotors, positions)

    return after_reverse


def main():
    config_name = input("Insert config(filename): ")
    rotor1, rotor2, rotor3, reflector = load_config(config_name)

    plugs = input("Insert plugs (y/n)?: ")
    if plugs.lower() == "y":
        # not implemented in this exercise
        print("Plugboard not implemented, skipping.")
    else:
        print("No extra plugs inserted.")

    print("Enigma initialized.\n")

    rotors = [rotor1, rotor2, rotor3]

    while True:
        row = input("Insert row (empty stops): ")
        if row == "":
            print("\nEnigma closing.")
            break

        # reset rotor positions for each new row
        positions = [0, 0, 0]

        converted_chars = []

        for ch in row:
            if ch.upper() in ALPHABET:
                original = ch.upper()
                illuminated = scramble_char(original, rotors, reflector, positions)
                print(f"Character \"{original}\" illuminated as \"{illuminated}\"")
                converted_chars.append(illuminated)
            else:
                # non-letter, keep as is
                converted_chars.append(ch)

        converted_row = "".join(converted_chars)
        print(f"Converted row - \"{converted_row}\".\n")


if __name__ == "__main__":
    main()
