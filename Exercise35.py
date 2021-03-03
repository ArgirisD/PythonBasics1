x = int(input("Please provide a number:"))
y = int(input("Please provide a second number:"))

def truth(x,y):
    diff = x - y
    sum = x + y
    if x == y or abs(diff) == 5 or sum ==  5:
        return True
    else:
        return False

print(truth(x,y))
