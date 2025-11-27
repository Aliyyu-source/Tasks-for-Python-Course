def main() -> None:
    Value = -1
    Sum = 0
    print("Program starting.")
    while Value != 0:
        Feed = input("Insert a floating-point value (0 to stop): ")
        try:
            Value = float(Feed)
            Sum = Sum + Value
        except Exception as err:
            print(f"Error! Could not convert {Feed} to float.")
            print(err)


    print("Program ending.")

main()