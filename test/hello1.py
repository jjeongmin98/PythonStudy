import re
p = re.compile('[a-z]+')

m1 = p.search('3 python')
#검색하는 함수

m2 = p.findall('life is too short')
#['life', 'is', 'too', 'short']

m3 = p.finditer('life is too short')
#<callable_iterator object at 0x000001A631877490>

m4 = p.match('python')
#start(): 시작점, group(): 전체출력 end(): 끝점, span(): 시작점과 끝점 출력

p1 = re.compile('a.b')
p2 = p1.match('a\nb')
#출력되지 않는다

p1 = re.compile('a.b', re.S)
p2 = p1.match('a\nb')
#Dot이 \n을 포함하기 때문에 출력이 가능하다.

p1 = re.compile('[a-z]', re.I)
#대소문자를 무시하고 매칭을 하도록 한다.

p1 = re.compile('^python\s\w+', re.M)
#문장이 바뀔때마다 새로운 문장으로 인식하도록 한다

print(m4.start())
    
