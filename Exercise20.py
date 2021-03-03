str = str(input("Please provide a string:"))
n = int(input("Please provide the number of times you want to see the string:"))

def multString(str, n):
    final = ""
    for number in range(n):
        final = final + str
    return final

print(multString(str, n))
