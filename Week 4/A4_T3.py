print("Program starting.")
print("")
Feed =input("Insert starting value: ")
Start =int(Feed)
Feed = input("Insert stopping value: ")
Stop = int(Feed)
print("")
print("Starting while-loop")
Current = Start
while Current != Stop:
    if(Current == (Stop)):
        print(Current)
    else:
        print(Current, end=' ')
    Current += 1
print("")
print("Program ending.")