f_string = str(input("Please provide a string:"))

def add_is(str):
    if len(str) >= 2 and str[:2] == "Is":
        return(str)
    else:
        l_string = "Is" + str
    return l_string

print(add_is(f_string))
