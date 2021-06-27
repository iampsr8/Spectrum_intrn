# Number of zeros in factorial
def zeros(n):
    c=0
    while(n>=5):
        c+=n//5
        n=n//5
    return c
x=int(input('Enter number: '))
print('Number of zeros in the factorial of '+ str(x)+ ' is '+ str(zeros(x)))
