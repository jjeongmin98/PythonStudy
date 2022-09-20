T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int,input().split())
    lst = [ list(map(int,input().split())) for _ in range (N)]
    rm_count=0
    hm_count=0
    for k in range (N): #가로 총합 구하기
        count =0
        for j in range (M):        
            if lst[k][j] == 1: 
                count +=1
            if lst[k][j] == 0 or j==M -1:
                j=M
            r_count=count
        if r_count > rm_count:
            rm_count = r_count

    for k in range (M): #가로 총합 구하기
        count =0
        for j in range (N):        
            if lst[j][k] == 1:
                count += 1
            if lst[j][k] == 0 or lst[j][k] == -1:
                k=j
            h_count =count
        if h_count > hm_count:
            hm_count = h_count    
    print("#{0} {1}".format(test_case,max(rm_count,hm_count)))


    
