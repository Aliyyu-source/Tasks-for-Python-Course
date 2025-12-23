########################################################
# Task A9_T7
# Developer Aliyyu Zen-Abdeen
# Date 2025-12-23
########################################################

import sys
import os  # for os.path.exists[web:303]

def showHelp() -> None:
    print("Invalid amount of arguments.")
    print("Usage: python A9_T7.py <src_file> <dst_file>")


def copyFile(src_file: str, dst_file: str) -> None:
    proceed = True

    # 1) Check if destination exists and ask before overwrite
    if os.path.exists(dst_file):  # test destination[web:303]
        answer = input(f'File "{dst_file}" exists. Overwrite (y/n)?: ').strip().lower()
        if answer != "y":
            print("Copy cancelled.")
            proceed = False

    if not proceed:
        return

    # 2) Try to copy, handle failure and exit with -1
    try:
        print(f'Source file "{src_file}"')
        print(f'Destination file "{dst_file}"')
        print(f'Copying file "{src_file}" to "{dst_file}".')

        with open(src_file, "r", encoding="utf-8") as src:
            content = src.read()
        with open(dst_file, "w", encoding="utf-8") as dst:
            dst.write(content)
    except Exception as e:
        print(f"Error during copy: {e}")
        sys.exit(-1)  # exit with error code on failure[web:307]


def main() -> None:
    print("Program starting.")

    # sys.argv: [script_name, src_file, dst_file][web:298][web:302][web:305]
    if len(sys.argv) != 3:
        showHelp()
        print("Program ending.")
        return

    src_file = sys.argv[1]
    dst_file = sys.argv[2]

    copyFile(src_file, dst_file)

    print("Program ending.")


if __name__ == "__main__":
    main()
