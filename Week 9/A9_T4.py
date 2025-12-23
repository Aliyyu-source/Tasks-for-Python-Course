########################################################
# Task A9_T4
# Developer Aliyyu Zen-Abdeen
# Date 2025-12-23
########################################################

TEMP_MIN = -273.15
TEMP_MAX = 10000


def collectCelsius() -> float:
    feed = input("Insert Celsius: ")
    # first: try to convert to float, otherwise raise ValueError
    try:
        celsius = float(feed)  # may raise ValueError[web:252][web:254][web:257]
    except ValueError:
        raise ValueError(f"could not convert string to float: '{feed}'")

    # second: check range, otherwise raise generic Exception
    if celsius < TEMP_MIN or celsius > TEMP_MAX:
        raise Exception(f"{celsius} temperature out of range.")

    return celsius


def main() -> None:
    print("Program starting.")
    celsius = collectCelsius()
    print(f"You inserted {celsius} °C")
    print("Program ending.")


if __name__ == "__main__":
    main()
