x = int(input("Please provide a number:"))
y = int(input("Please provide a second number:"))
z = int(input("Please provide a third number:"))

if x != y and y != z and x != z:
    sum = x + y + z
    print(sum)
else:
    print(0)
