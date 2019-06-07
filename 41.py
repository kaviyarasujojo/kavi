string=input().split()
for i in string:
    if(i.isdigit()):
        c=int(i)
for i in string:
    if(i.isalpha()):
        s=i
for i in range(0,c):
    print(s)
