sum = int(input(""))
n = int(input(""))
nsum=0
lst=[]
lst1=[]
for i in range(0,n):
    A, B= map(int,input("").split())
    lst.append(A)
    lst1.append(B)
for k in range(0,n):
    nsum +=lst[k] * lst1[k]
if nsum == sum:
    print("Yes")
else:
    print("No")