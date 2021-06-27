# First n perfect numbers
x=int(input('Enter number: '))
a=2
b=1
s=0
c=0
while (c<x):
    while(b<a):
        if(a%b==0):
            s+=b
        b+=1
    if(s==a):
        print(a,end=" ")
        c+=1
    a+=1
    b=1
    s=0
    