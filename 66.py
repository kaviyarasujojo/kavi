s=int(input())
c=0
for i in range(1,s+1):
    if(s%i==0):
        c=c+1
if(c==2):
    print('yes')
else:print('no')
