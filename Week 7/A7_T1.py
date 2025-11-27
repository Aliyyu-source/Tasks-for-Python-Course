def askPositiveInteger() -> int:
    PositiveInt = -1
    Feed = input("Insert positive Integers (negative stops): ")
    if Feed.isnumeric():
        PositiveInt = int(Feed)
    return PositiveInt #return the number if it is numeric

def displayIntegers(Numbers: list[int]):
    if len(Numbers) == 0: # if the list is empty
        print("No integers to display.")
    else:
        print(f"Displaying {len(Numbers)} integers: ")
        for i in range(len(Numbers))
    return None

def main():
    print("Program starting.")
    print("Collect positive integers.")
    PositiveIntegers: list[int] = []
    CurrentInteger = askPositiveInteger() #jump to ask first positive integer
    while CurrentInteger >= 0:
        PositiveIntegers.append()
        CurrentInteger = askPositiveInteger()
    print("Stopped collecting positive integers.")
    displayIntegers(PositiveIntegers)

    return None

