def solution(n, m):
    nlist=[]
    mlist=[]
    tlist=[]
    count =0
    mmx=0
    dlist=[]
    for i in range(1, n+1):
        if n % i == 0:
            nlist.append(i)
    for i in range(1, m+1):
        if m % i == 0:
            mlist.append(i)
    for i in range(len(mlist)):
        for k in range(len(nlist)):
            if mlist[i] == nlist[k]:
                tlist.append(mlist[i])

    for i in range(1,max(n,m)):
        for k in range(1,max(n,m)):
            if n*i == k*m:
                dlist.append(n*i)
    dlist.append(n*m)
    
    return [max(tlist), min(dlist)]
                     
     
