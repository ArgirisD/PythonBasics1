def concentrate (list):
    sum = ""
    for item in list:
        sum = sum + str(item)
    return(sum)

list = [1, "arg", 0.7, "dimi"]
print(concentrate(list))
