print("Program starting")
print("Insert two integers")
A  = int(input("Insert first integer:  "))
B = int(input("Insert second integer: "))
print("Comparing inserted integers")
if A > B:
    print("first integer is greater")
elif A == B:
    print("Intergers are the same")
else:
    print("second integer is greater")
print("Adding integers together")
Sum =(f"{A} + {B} = {A + B}")
print(Sum)
Parity =(A % B )
if Parity == 0:
    print("It is even")
else:
    print("t is odd")
print("Program ending.")
