# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.
A =int(input(""))
if A>=90 and A<=100:
    print("A")
elif A>=80 and A<=89:
    print("B")
elif A>=70 and A<=79:
    print("C")
elif A>=60 and A<=69:
    print("D")
else:
    print("F")
