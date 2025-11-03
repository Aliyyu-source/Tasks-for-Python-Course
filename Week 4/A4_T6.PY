print("Program starting.")
u = int(input("Insert a positive integer:  "))
s = [u]
st = 0
while u != 1:
    if u % 2 == 0:
        u = u // 2
    else:
        u = 3 * u + 1
    s.append(u)
    st += 1
output = ""
for i in range(len(s)):
    output += str(s[i])
    if i < len(s) - 1:
        output += " -> "
print(output)
print("Sequence had", st, "total steps.\n")
print("Program ending.")
