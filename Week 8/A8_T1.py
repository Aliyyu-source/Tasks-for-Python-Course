import time

def print_menu():
    print("Options:")
    print("1 - Set pause duration")
    print("2 - Activate pause")
    print("0 - Exit")

def main():
    print("Program starting.")
    pause_duration = 0.0  # seconds

    while True:
        print_menu()
        choice = input("Your choice: ")

        if choice == "1":
            # set pause duration
            value = input("Insert pause duration (s): ")
            try:
                pause_duration = float(value)
            except ValueError:
                # if user types something not a number, keep old value
                pause_duration = 0.0
            print()

        elif choice == "2":
            # activate pause
            print(f"Pausing for {pause_duration} seconds.")
            time.sleep(pause_duration)  # pause here[web:171][web:172][web:175][web:178]
            print("Unpaused.\n")

        elif choice == "0":
            print("Exiting program.\n")
            break

        else:
            # invalid option, just show menu again
            print("Invalid choice.\n")

    print("Program ending.")

if __name__ == "__main__":
    main()
