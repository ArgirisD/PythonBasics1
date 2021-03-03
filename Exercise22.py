numbers = input("Please provide a list of numbers separated by comma:")
list = numbers.split(",")
counter = 0
for num in list:
    if int(num) == 4:
        counter = counter + 1
print(counter)
