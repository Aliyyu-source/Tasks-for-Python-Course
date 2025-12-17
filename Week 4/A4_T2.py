print("Program starting")
First =int(input("Insert starting value: "))
Second =int(input("Insert stopping value: "))
print("Starting for loop:")

for x in range(First ,Second):
    if x == Second -1:
        print(x)
    else:
        print(x, end=" ")

print("Program ending")
