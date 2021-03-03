h = float(input("Please provide the height of the triangle:"))
b = float(input("Please provide the base of the triangle:"))

def triangleArea(h, b):
    A = h*b/2
    return A

print("The area of the triangle is:", triangleArea(h,b))
