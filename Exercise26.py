nums = input("Please provide a list of numbers separated by comma:")
list = nums.split(",")

def histo (list):
    for number in list:
        histogram = ""
        count = int(number)
        while count > 0:
            histogram = histogram + "@"
            count = count - 1
        print(histogram)

histo(list)
