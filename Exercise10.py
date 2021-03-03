n = int(input("Please provide a number to receive its factor:"))
n1 = int("%s" % n)
n2 = int("%s%s" % (n,n))
n3 = int("%s%s%s" % (n,n,n))
factor = n1 + n2 + n3 # NOTE: That is one way to do it.
print(factor)
