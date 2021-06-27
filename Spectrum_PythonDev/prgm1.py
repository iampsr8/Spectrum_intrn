# Case change higher to lower vice versa
phrase=input("Enter phrase: ")
l=[]
for i in phrase:
    if(i.isupper()):
        l.append(i.lower())
    else:
        l.append(i.upper())    
for i in l:
    print(i,end="")