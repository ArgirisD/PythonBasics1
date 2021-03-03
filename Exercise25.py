n = int(input("Please provide the number you want to check:"))
values = [1,5,8,3]

def check (n, values):
    return n in values

print(check(n,values))
