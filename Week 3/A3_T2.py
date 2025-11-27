print("Program starting")
print("string comparisons")
Word1 = input("Insert first word: ")
Character = input("Insert a character: ")
if Character in Word1:
    print(f" word {Word1} contains character {Character}")
else:
    print(f" word {Word1} doesn't contain character {Character}")

Word2 = input("Insert second word: ")
print("Comparing Word1 to Word2")
if Word2 > Word1:
    print(f"The first word {Word1} is before the second word {Word2} alphabetically")
elif Word1 == Word2:
    print(f"Both inserted words are the same alphabetically {Word1}")
else:
    print(f"The second word {Word2} is before the first word {Word1} alphabetically")
print("Program ending.")