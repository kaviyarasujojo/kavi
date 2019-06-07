n=int(input())
b=list(map(int,input().split()))
d=0
b.sort()
for i in range(0,n):
    c=int(b[i])
    d=c+d
avg=d/n
print(avg)

