# Constant delimiter used between words
DELIMITER = ','


def collectWords() -> str:
    """
    Collect words from user until an empty word is given.
    Returns a single string with words separated by DELIMITER.
    """
    words = []

    while True:
        word = input("Insert word(empty stops): ")
        if word == "":
            break
        words.append(word)

    # Join all collected words with the delimiter into one string
    return DELIMITER.join(words)


def analyseWords(PWords: str) -> None:
    """
    Analyse the collected words:
    - number of words
    - total characters (without delimiters)
    - average word length (2 decimal precision)
    Prints the results and returns None.
    """
    if PWords == "":
        # No words given
        word_count = 0
        char_count = 0
        avg_length = 0.0
    else:
        # Split using the delimiter constant
        word_list = PWords.split(DELIMITER)
        word_count = len(word_list)
        # Count characters in all words (without delimiter)
        char_count = sum(len(w) for w in word_list)
        if word_count > 0:
            avg_length = char_count / word_count
        else:
            avg_length = 0.0

    print(f"- {word_count} Words")
    print(f"- {char_count} Characters")
    print("- {:.2f} Average word length".format(avg_length))
    return None


def main() -> None:
    """Main program logic."""
    print("Program starting.")
    words = collectWords()
    analyseWords(words)
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
