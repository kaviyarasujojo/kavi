alist=[]
n=int(input("enter the size of array"))
for i in range(0,n,1):
  item=int(input("enter the items"))
  alist.append(item)
for j in range(0,n,1):
  print(alist[j],"[",j,"]")

