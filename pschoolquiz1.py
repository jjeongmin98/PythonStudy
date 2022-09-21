def solution(left, right):
    sum=0
    for i in range(left,right+1): #left~right
        count = 1
        for k in range(1,i): #left 약수
            if i % k == 0:
                count +=1 #약수의 개수
        if count % 2 != 0:
            i = i * -1
        sum = sum+i
                        
    return sum
