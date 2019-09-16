from random import randint
l = []
for i in range(10):
    l.append(randint(1,100))
print(l)
x = int(l[i])
y=l[0]
pos=i
while (i>0):
    i=i-1
    if l[i]<x:
        x = int(l[i])
        pos=i
l[0]=x
l[pos]=y
print(l)
