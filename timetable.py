#구구단 프로그램 by 김정민(eodjr05@naver.com)
k=1
con = 1
print("///김정민의 구구단 프로그램 ////")

while con:
    num=0
    n=0
    con = int(input("몇단을 진행할까요? (정지:0) \n"))
    if con>0:
        while n<10:
            print("%d * %d = %d 입니다."%(con, n, con*n))
            n=n+1
    else:
        break
    
 
