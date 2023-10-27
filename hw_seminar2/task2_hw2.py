'''
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
Примечание: числа S и P задавать не нужно, они будут передаваться в тестах. В результате вы должны вывести все возможные пары чисел X и Y через пробел, такие что X <= Y.

Пример

На входе:

s = 12
p = 27
На выходе:
3 9
'''


s = 4
p = 4
#print(4**2)
#print(round(3**(0.5),2))
b = -s
d = s**2-4*p
x1 = (-b+d**0.5)/2
x2 = (-b-d**0.5)/2
#print(x1, x2)
y1 = s-x1
y2 = s-x2
#print(y1,y2)
for i,j in (x1,y1),(x2,y2):
    if i<=j:
        print(int(i),int(j))
    if i==j:
        break

'''
Другой вариант(перебор)
for i in range(s//2+1):
    if i*(s-i) == p:
        print(i, s-i)
'''