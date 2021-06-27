# Star pattern
for i in range(5):
    for k in range(2*i):
        print(' ',end="")
    for j in range(5-i):
        print('  *',end=" ")
    print()
for i in range(5):
    if(i==0):
        i+=1
        continue
    for k in range(2*(4-i)):
        print(' ',end="")
    for j in range(i+1):
        print('  *',end=" ")
    print()