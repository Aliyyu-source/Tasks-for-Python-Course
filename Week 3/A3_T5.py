print("program starting /n") 
print ("options")
print("  1. Celsius to Fahrenheit")
print (" 2. Fahrenheit to Celsius")
print (" 0. Exit")
a = int(input("if temperature is /n "))

if temperature == 1:
  b = float(input("Insert the amount of Celsius"))
  c = round((b * 1.8) + 32, 1)
  print(f"{b} °C equals to {c} °F \n")
elif a ==2:
  d = float(input("Insert the amount of Fahreheit: "))
  e = round((d-32) /1.8,1)
  print (f"{d} °F equals to {e} °C \n")
elif a == 0:
  print("Exiting...\n")
else:
  print("Unknown option. \n")

print ("Program ending")