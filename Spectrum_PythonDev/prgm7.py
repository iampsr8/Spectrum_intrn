# triplet sum equal to the given sum
def triplet(a,n,s):
    for i in range(n):
        for j in range(1,n):
            for k in range(2,n):
                if(a[i]+a[j]+a[k]==s):
                    print(a[i], a[j], a[k])
                    return True
    return False
a=[]
n=int(input('Enter number of elements in array'))
print('Enter elements in the array: ')
for i in range(n):
    a.append(int(input()))
s=int(input('Enter sum'))
triplet(a,n,s)