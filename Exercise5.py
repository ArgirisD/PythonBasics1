FullName = input("Please provide your full name:")
NameList = FullName.split()
print("Hello ", *reversed(NameList))
