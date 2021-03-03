str = str(input("Please provide your string:"))
n = int(input("Please provide the number of copies:"))

def check(str,n):
    final = ""
    if len(str) < 2:
        for i in range(n):
            final = final + str
        print(final)
    else:
        for i in range(n):
            final = final + str[0:2]
        print(final)

check(str,n)
