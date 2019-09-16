import math
n=int(input("enter a number greater than 1:"))
if (n>1):
    if (2**int(math.log(n,2))==n):
        print("Y")
    else:
        print("N")
else:
    n=int(input("enter a number greater than 1:"))
