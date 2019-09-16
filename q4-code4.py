n=int(input("Input a number greater than 1:"))
lpf=[]
for i in range(2,n+1):
    while(n/i>1 and n%i==0):
        lpf.append(i)
        n=int(n/i)
    if (n/i==1):
        lpf.append(n)
print(lpf)
