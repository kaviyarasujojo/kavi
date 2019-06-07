n=[]
for i in range(0,2):
    n1=input()
    n.append(n1)
c=n[0]
n[0]=n[1]
n[1]=c
for i in n:
    print(i)
