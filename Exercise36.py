x = int(input("Please provide a number:"))
y = int(input("Please provide a second number:"))

def add_integers(x,y):
    if not (isinstance(x, int) and isinstance(y, int)):
        return TypeError("Input must be integers!")
    return x+y

print(add_integers(x,y))
print(add_integers(4.3,5.6))
