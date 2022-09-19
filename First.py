from random import *
lst = list(range(1,21))
shuffle(lst)
winner = sample(lst,3)
print("치킨 당첨자 {0}".format(winner[0]))
print("커피 당첨자 {0}".format(winner[1:3]))
print("아님")