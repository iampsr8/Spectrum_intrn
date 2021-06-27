# gcd of given array
def gcd(x,y):
    if(x==0):
        return y
    if(y==0):
        return x
    if(x==y):
        return x
    if(y>x):
        return gcd(x,y-x)
    return gcd(x-y,y)
a=[]
b=int(input("Enter size of array: "))
print('Enter elements in the array')
for i in range(b):
    a.append(int(input()))
g=gcd(a[0],a[1])
for i in range(2,b):
    g=gcd(g,a[i])
print('gcd = ' + str(g))