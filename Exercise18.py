num = input("Please provide three numbers separated by a comma:")
num = num.split(",")
sum = 0
for number in num:
    sum = sum + int(number)
if num[0] == num[1] and num[1] == num[2]:
    sum = sum*3
    print(sum)
else:
    print(sum)
