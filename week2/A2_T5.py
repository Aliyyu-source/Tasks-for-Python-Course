#print("Program starting")
#word = input("Enter a compound word: ")
#print(len(word))
#print(word[0])
#print(word[::-1])

#print(f"The inserted word length is {len(word)}")
#print(f"The first character is {word[0]}")
#print(f"The reversed version is {word[::-1]}")

#print("Prompt for a substring")
#A =int(input("Enter the start index for substring:  "))
#B =int(input("Enter the end index for substring:  "))
#C =int(input("Enter the step size for substring: "))

#print(f"The {word}")
#print(f"sliced to the defined substring is {word[:4]} ")
#print("Program ending")


print("Program starting.")

# Prompt for compound word
word = input("Insert a closed compound word: ")

# Display word details
reversed_word = word[::-1]
print(f"The word you inserted is '{word}' and in reverse it is '{reversed_word}'.")
print(f"The inserted word length is {len(word)}")
print(f"Last character is '{word[-1]}'")

# Prompt for substring details
print("\nTake substring from the inserted word by inserting...")
start = int(input("1) Starting point: "))
end = int(input("2) Ending point: "))
step = int(input("3) Step size: "))

# Slice and display substring
substring = word[start:end:step]
print(f"\nThe word '{word}' sliced to the defined substring is '{substring}'.")

print("Program ending.")
