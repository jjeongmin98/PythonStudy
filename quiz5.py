# quiz) 당신은 cocoa 서비스를 이용하는 택시 기사이다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오

# 조건 1 ; 승객별 운행 소여 시간은 5분 ~ 50 분 사이의 난수로 정해진다.
# 조건 2 : 당신은 소요시간 5분 ~ 15분 사이의 승객만 매칭해야한다.
# //출처 : 나도코딩

from random import *
count = 0
for i in range(1,51):
    n = int(randrange(5,50))
    if n in range(5,15):
        print("[o] {0}번째 손님 (소요시간 : {1}분".format(i,n))
        count += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분".format(i,n))
print("총 탑승 승객 : {0}분".format(count))
