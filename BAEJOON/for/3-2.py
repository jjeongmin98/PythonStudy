T = int(input(""))
lst=[]
lst2=[]
for i in range(0,T):
    A,B = map(int,input("").split())
    lst.append(A)
    lst2.append(B)
for k in range(0,T):
    print(lst[k]+lst2[k])
