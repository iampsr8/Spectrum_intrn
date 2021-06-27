# All prime numbers till n
x=int(input('Enter number'))
i=2
k=0
while (k<=x):
    while(i<k):
        if(k%i==0):
            break
        i+=1
    if(i==k):
        print(k,end=' ')
        i=2
    k+=1