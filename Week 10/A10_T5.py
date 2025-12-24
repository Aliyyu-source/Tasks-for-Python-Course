########################################################
# Task A10_T5
# Developer Aliyyu Zen-Abdeen
# Date 2025-12-24
########################################################


def recursiveFactorial(PNum: int) -> int:
    """Return n! computed recursively."""
    # Base case: 0! and 1! are 1[web:356][web:359][web:361][web:363]
    if PNum == 0 or PNum == 1:
        return 1
    # Recursive step: n! = n * (n-1)![web:356][web:359][web:361][web:363]
    return PNum * recursiveFactorial(PNum - 1)


def main() -> None:
    print("Program starting.")
    user_input = input("Insert factorial: ")

    # Convert input to int (no error handling specified in task)
    n = int(user_input)

    result = recursiveFactorial(n)

    print(f"Factorial {n}!")
    print(f"{n} = {result}")
    print("Program ending.")


if __name__ == "__main__":
    main()
