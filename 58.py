p1,p2=input().split()
p1=int(p1)
p2=int(p2)
c=0
temp=list(map(int,input().split()))
for i in temp:
    if(i==p2):
        c=c+1
        break
if(c!=0):
    print("Yes")
else:print("No")
