# nth smallest integer in the array
a=[]
x=int(input('Enter number of elements in array: '))
print('Enter elements in the array: ')
for i in range(x):
    a.append(int(input()))
a.sort()
n=int(input('Enter integer n: '))
print(a[n-1])