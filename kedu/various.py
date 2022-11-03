def solution(x):
    for k in range(0,len(x)):
        for i in range(0,len(x)):
            if i[i] == 1:
                if i[i-1] == 3:
                    if i[i-2] == 2:
                        if i[i-3] == 1:
                            cnt+=1
                            
    return cnt