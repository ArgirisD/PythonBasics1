x = int(input("Please provide a number:"))
y = int(input("Please provide a second number:"))

def gcd(x,y):
    gcd = 1
    if x % y == 0:
        return y
    for k in range(int(y / 2), 0, -1):
        if x % k == 0 and y % k == 0:
            gcd = k
            break
    return gcd

def lcm(x,y,gcd):
    m = x*y
    lcm = abs(m)/gcd
    return lcm

gcd = gcd(x,y)
print(lcm(x,y,gcd))
