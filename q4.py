from random import randint
list();
y=input("enter a number:")
y=int(y);
m=0
for i in range(3):
    print(y);
    for i in range(3):
        x=randint(1,5);
        m=m+x;
        print(x);
print(m);
        
