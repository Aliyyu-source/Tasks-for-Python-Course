def main():
    print("Program starting.")
    print()
    print("Check multiplicative persistence.")

    # Ask user for the starting integer
    n_str = input("Insert an integer: ")
    n = int(n_str)  # assume valid integer as in example
    print()

    steps = 0

    # Keep going while n has more than one digit
    while n >= 10:
        digits_str = str(n)

        # Build the left-hand side like: 2 * 7 * 7 * ...
        parts = []
        product = 1
        for ch in digits_str:
            d = int(ch)
            parts.append(str(d))
            product *= d

        left_side = " * ".join(parts)
        print(f"{left_side} = {product}")

        n = product
        steps += 1

    print("No more steps.")
    print()
    print(f"This program took {steps} step(s)")
    print()
    print("Program ending.")


if __name__ == "__main__":
    main()
