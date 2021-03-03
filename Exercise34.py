x = int(input("Please provide a number:"))
y = int(input("Please provide a second number:"))

def sum (x,y):
    sum = x + y
    if sum in range(15,20):
        sum = 20
    return sum

print(sum(x,y))
