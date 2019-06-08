v1=int(input())
n=v1
c=0
while (n!=1):
    n=n//2
    c=c+1
t1=2**c
if (v1==t1):
    print("yes")
else:
    print("no")
