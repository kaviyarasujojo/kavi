string = input()
c=0
s=0
for i in range(len(string)):
    if(string[i].isalpha() or string[i].isdigit()):
       c=c+1
    else:
        s=s+1
print(s)
