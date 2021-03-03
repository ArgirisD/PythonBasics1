x = int(input("Please provide a number:"))
y = int(input("Please provide a second number:"))

def multiplication(x,y):
    f = (x+y)**2
    return f

print("({} + {})^2 = {}".format(x,y,multiplication(x,y)))
