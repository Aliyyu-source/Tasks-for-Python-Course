########################################################
# Task A9_T1
# Developer Aliyyu Zen-Abdeen
# Date 2025-12-23
########################################################

def main() -> None:
    print("Program starting.\n")

    total = 0.0

    while True:
        value_str = input("Insert a floating-point value (0 to stop): ")
        if value_str == "0":
            break

        try:
            value = float(value_str)  # may raise ValueError[web:252][web:254][web:257]
            total += value
        except ValueError:
            print("Error! '{}' couldn't be converted to float.".format(value_str))

    print("\nFinal sum is {:.2f}".format(total))  # two decimal places[web:255][web:258]
    print("Program ending.")


if __name__ == "__main__":
    main()

