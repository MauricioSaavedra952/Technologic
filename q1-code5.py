from random import randint
l = []
for i in range(10):
    l.append(randint(1,100))
x = int(l[i])
pos=i
while (i>0):
    i=i-1
    if l[i]<x:
        x = int(l[i])
        pos=i
print(l)
print("the min value is: ", x)
print("its index is: ", pos)
