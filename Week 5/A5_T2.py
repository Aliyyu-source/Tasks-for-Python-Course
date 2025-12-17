def frameWord(PWord):
    """Print the given word inside a decorative asterisk frame."""
    # Length of the word plus spaces and asterisks: 2 spaces + 2 asterisks
    frame_length = len(PWord) + 4
    print("*" * frame_length)
    print(f"* {PWord} *")
    print("*" * frame_length)


def main():
    """Main function: handles input and overall program messages."""
    print("Program starting.")
    print()  # empty line

    word = input("Insert word: ")

    print()  # empty line before frame
    frameWord(word)
    print()  # empty line after frame

    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
