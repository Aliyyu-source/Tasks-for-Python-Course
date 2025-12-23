########################################################
# Task A9_T3
# Developer Aliyyu Zen-Abdeen
# Date 2025-12-23
########################################################

import sys  # for sys.exit[web:265]

def main() -> None:
    print("Program starting.")
    filename = input("Insert filename: ")

    try:
        with open(filename, "r", encoding="utf-8") as f:
            print(f"## {filename} ##")
            for line in f:  # read and print line by line[web:266][web:269]
                print(line.rstrip())
            print(f"## {filename} ##")
    except FileNotFoundError:
        print(f"Error! File '{filename}' not found.")
        sys.exit(1)  # exit with error code 1[web:265][web:268]

    print("Program ending.")


if __name__ == "__main__":
    main()
