from random import randint
for i in range(10):
    x=randint(1,100)
    print(x)
    if x % 6 == 0:
        print(x,"divisible by 2")
        print(x,"divisible by 6")
    elif x%2 == 0:
        print(x,"divisible by 2")
