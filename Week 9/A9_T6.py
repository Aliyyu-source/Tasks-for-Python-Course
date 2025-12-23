########################################################
# Task A9_T6
# Developer Aliyyu Zen-Abdeen
# Date 2025-12-23
########################################################

def print_menu() -> None:
    print("Options:")
    print("1 - Insert line")
    print("2 - Save lines")
    print("0 - Exit")


def insert_line(lines: list[str]) -> None:
    text = input("Insert text: ")
    lines.append(text)
    print()


def save_lines(lines: list[str]) -> None:
    if not lines:
        print("No lines to save.\n")
        return

    filename = input("Insert filename: ")
    with open(filename, "w", encoding="utf-8") as f:
        for line in lines:  # write each line on its own line[web:293]
            f.write(line + "\n")
    print("Lines saved.\n")


def run_menu() -> None:
    lines: list[str] = []

    while True:
        print_menu()
        choice = input("Your choice: ")

        if choice == "1":
            insert_line(lines)
        elif choice == "2":
            save_lines(lines)
        elif choice == "0":
            print("Program ending.")
            return
        else:
            print("Invalid choice.\n")


def main() -> None:
    print("Program starting.")
    lines: list[str] = []

    try:
        # reuse the same list in run loop
        while True:
            print_menu()
            choice = input("Your choice: ")

            if choice == "1":
                insert_line(lines)
            elif choice == "2":
                save_lines(lines)
            elif choice == "0":
                print("Program ending.")
                return
            else:
                print("Invalid choice.\n")

    except KeyboardInterrupt:
        # user pressed Ctrl+C (KeyboardInterrupt)[web:291][web:295]
        if not lines:
            print("Keyboard interrupt and no unsaved lines. Closing program.")
            return

        print("Keyboard interrupt and unsaved progress!")
        answer = input("Save before quit(y/n)?: ").strip().lower()

        if answer == "y":
            filename = input("Insert filename: ")
            with open(filename, "w", encoding="utf-8") as f:
                for line in lines:
                    f.write(line + "\n")  # save collected lines[web:293]
        # end whether saved or not
        print("Program ending.")


if __name__ == "__main__":
    main()
