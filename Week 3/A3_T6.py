print("Program starting")
print("Welcome to the unit converter program!")
print("Follow the menu instructions below. \n")
print("Options:")
print("1-Length")
print("2-Weight")
print("0-Exit")

main_choice =int(input("Your choice:"))

if main_choice ==2:
 print("\nWeight options:")
 print("1- Grams to pounds")
 print("2- Pounds to grams")
 print("0- Exit")
 weight_option=int(input("Your choice: "))
if weight_option ==2:
 pounds_val=float(input("Insert pounds: "))
 grams_val=round(pounds_val*453.6,1)
 print(f"{pounds_val} lb is {grams_val} g")
elif weight_option==1:
 grams_val=float(input("Insert grams:"))
 pounds_val=round(grams_val/453.6 ,1)
 print(f"{grams_val} g is {pounds_val} lb")
elif weight_option==0:
 print("Exiting...")
else:
 print("Unknown option.")

if main_choices==1:
 print("\nLength options:")
 print("1- Meters to kilometers")
 print("2- Kilometers to meters")
 print("0- Exit")
 length_option=int(input("Your choice: "))
if length_option==2:
 km_val=float(input("Insert kilometers: "))
 m_val=km_val*1000
 print(f"{km_val} km is {m_val} m")
elif length_option==1:
 m_val=float(input("Insert meters:"))
 km_val=m_val/1000
 print(f"{m_val} m is {km_val}km")
elif length_option==0:
 print("Exiting...")
else:
 print("Unknown option.")

if main_choice==0:
 print("Exiting...")
else:
 print("Unknown option.")

print ("\nProgram ending.")

