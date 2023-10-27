'''
Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числаN.

Пример

n=16

#Вывод
1
2
4
8
16
'''


n = 1
'''
res = 1
count=1
while res<=n:
    print(res)
    res=2**count
    count += 1
'''
res = 1
while res<=n:
    print(res)  #print(res, end=' ')
    res *= 2