########################################################
# Task A9_T2
# Developer Aliyyu Zen-Abdeen
# Date 2025-12-23
########################################################

import sys  # for sys.exit[web:1]

def main() -> None:
    print("Program starting.")
    code_str = input("Insert exit code(0-255): ")
    code = int(code_str)  # convert to int[web:252]

    if code == 0:
        print("Clean exit\n")
    else:
        print(f"Exit with code {code}\n")

    sys.exit(code)  # exit using user-defined code (0–255)[web:1]


if __name__ == "__main__":
    main()
