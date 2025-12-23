########################################################
# Task A9_T5
# Developer Aliyyu Zen-Abdeen
# Date 2025-12-23
########################################################

def main() -> None:
    print("Program starting.")

    try:
        r_str = input("Insert red: ")
        g_str = input("Insert green: ")
        b_str = input("Insert blue: ")

        # check numeric + integer
        r = int(r_str)
        g = int(g_str)
        b = int(b_str)  # will raise ValueError if not integer text[web:284][web:287]

        # check range 0–255
        for value in (r, g, b):
            if value < 0 or value > 255:
                raise ValueError("out of range")

        # if all ok, display details
        print("RGB Details:")
        print(f"- Red {r}")
        print(f"- Green {g}")
        print(f"- Blue {b}")

        # hex string #rrggbb with 2-digit lowercase hex each[web:278][web:279][web:280][web:282]
        hex_code = "#{:02x}{:02x}{:02x}".format(r, g, b)
        print(f"- Hex {hex_code}")

    except Exception:
        # any invalid input or range problem
        print("Couldn't perform the designed task due to the invalid input values.")

    print("Program ending.")


if __name__ == "__main__":
    main()
