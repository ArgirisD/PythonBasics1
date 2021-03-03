num = int(input("Please provide a number:"))

def check(num):
    x = num % 2
    if x > 0:
        return print("The number is odd.")
    else:
        return print("The number is even.")

check(num)
