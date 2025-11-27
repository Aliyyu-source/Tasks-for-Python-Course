print("Program starting.")
print("This is a program with simple menu, where you can choose which operation the program performs.")
Name =input("Before the menu, please insert your name: ")
print ("John")

print("options")
print("1 - Print welcome message")
print("2 - Print the name backwards")
print("3 - Print the first character")
print("4 - Show the amount of characters in the name")
print("0 - Exit")

Feed = input("Your choice: ")
Choice = int(Feed)

if(Choice == 1):
    print(f"Welcome {Name}!")
elif(Choice == 2):
    print(f"Your name backwards is {Name[::-1]}")
elif(Choice == 3):
    print(f"The first character in {Name} is {Name[0]}")
elif(Choice == 4):
    print(f"There are {len(Name)} characters in the name {Name}")
elif(Choice == 0):
    print("Exiting...")
else:
    print("Unknown option.")

print("Program ending.")    
