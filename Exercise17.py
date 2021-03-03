x = int(input("Please enter your number:"))

def question(x):
    return (abs(1000-x) <= 100) or (abs(2000-x) <= 100)

print(question(x))
