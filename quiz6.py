# quiz ) 표준 체중을 구하는 프로그램을 작성하시오

# * 표준 체중 : 각 개인의 키에 적당한 체중
# (성별에 따른 공식)
# 남자 : 키(m) * 키(m) * 22
# 여자 : 키(m) * 키(m) * 21

# 조건 1: 표준 체중은 별도의 함수 내에서 계산
# 함수명 : std_weight
# 전닯갓 : 키(height), 성별(gender)

# 조건 2 : 표준 체중은 소수점 둘째자리까지 표시

# (출력 에제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.

def std_weight(height, gender):
    if gender == 'm':
        return height * height * 22
    else:
        return height * height * 21

gender = input("성별이 무엇입니까 (남성 : m , 여성 : w )\n")
height = int(input("키는 어떻게 되십니까(m)"))
stand = round(std_weight(height / 100,gender),2)
print("키 {0}cm 남자의 표준 체중은 {1}입니다.".format(height,stand))