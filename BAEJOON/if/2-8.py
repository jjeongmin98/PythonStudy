A,B,C = map(int,input("").split())
lst=[]
lst.append(A)
lst.append(B)
lst.append(C)
if len(set(lst))==3:
    print("{0}".format(max(lst)*100))
elif len(set(lst))==2:
    if A==B:
        print("{0}".format(1000+(A*100)))
    elif B==C:
        print("{0}".format(1000+(B*100)))
    else:
        print("{0}".format(1000+(A*100)))
else:
    print("{0}".format(10000+(A*1000)))