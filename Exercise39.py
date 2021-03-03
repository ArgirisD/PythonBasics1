amt = float(input("Please provide the specific ammount:"))
interest = float(input("Please provide the related interest per cent %:"))
y = int(input("Please provide the number of years to compute:"))

def intrCalc(amt, interest, y):
    count = 0
    while count < y:
        amt = amt + amt*(interest/100)
        count = count +1
    return (amt)

total = intrCalc(amt, interest, y)
print(total)
