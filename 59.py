p=int(input())
c=1
for i in range(0,p):
    p=p//10
    if(p!=0):
        c=c+1
print(c)
