# Number of times string f occurs in string s
def occurs(s,f):
    a=len(s)
    b=len(f)
    r=0
    for i in range(a-b+1):
        j=0
        while (j<b):
            if(s[i+j]!=f[j]):
                break
            j+=1
        if(j==b):
            r+=1
            j=0
    return r
s=input('Enter string S: ')
f=input('Enter string F: ')
print(str(occurs(s,f)))
