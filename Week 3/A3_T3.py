print("Program starting")
Username =input("Prompt username first: ")

print("1- Welcome message")
print("0- Exit")
option = int(input("Choose your choice:  "))

if option == 1:
    print(f"Welcome {Username}")
elif option == 0:
    print("Exiting...")
else:
    print("Unknown option")
print("Program ending.")