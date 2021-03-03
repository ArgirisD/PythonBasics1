import math

x = input("Please provide the coordinates of point x splitted by a comma:")
y = input("Please provide the coordinates of point y splitted by a comma:")

x = x.split(",")
y = y.split(",")

dist = math.sqrt((int(x[1])-int(x[0]))**2 + (int(y[1])-int(y[0]))**2)
print(dist)
