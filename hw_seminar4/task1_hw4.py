'''
Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
На вход подается 2 числа через пробел: n m
n - кол-во элементов первого множества.
m - кол-во элементов второго множества.
Затем подаются элементы каждого множества через пробел в виде строки. ! Писать input() не надо

Пример

На входе:


var1 = '5 4' # количество элементов первого и второго множества
var2 = '1 3 5 7 9' # элементы первого множества через пробел
var3 = '2 3 4 5' # элементы второго множества через пробел
На выходе:

3 5
'''

var1 = '5 4' # количество элементов первого и второго множества
var2 = '1 25 30 40 58 55 9'# элементы первого множества через пробел
var3 = '11 20 30 1 50 24 78 9 1 ' # элементы второго множества через пробел
# print(f'{var1}\n{var2}\n{var3}')
a = set(var2.split())
b = set(var3.split())
inters = a.intersection(b)  # inters= a & b даст аналогичный результат (было на семинаре)
#print(inters)
list_inters = list(inters)
#print(list_inters)
for i in range(len(list_inters)):        # list_inters = [int(i) for i in inters]
    list_inters[i] = int(list_inters[i]) 
#print(list_inters)
# вместо сортировки выбором можно было бы написать result=sorted(inters) - сортед переводит множество в список
# и сортирует его (было на семинаре)
count = len(list_inters)
if count!=0: 
    while count!=1:          # сортировка методом выбора
        max = list_inters[0]
        max_index = 0
        for i in range(1,count):
            if list_inters[i]>max:
                max=list_inters[i]
                max_index = i
        list_inters.insert(count-1,list_inters.pop(max_index))
        count-=1
#print(list_inters)
for i in list_inters:
    print(i,end=' ')
# print(*inters) - множестов распакуется без скобок, значения будут идти через пробел (было на семинаре)

# что подставляет автотест:
# 1) var1 = '3 4'
# var2 = '1 2 3'
# var3 = '1 2 3 4'
# 2) var1 = '4 4'
# var2 = '5 6 7 8' 
# var3 = '6 7 8 9'
# 3) var1 = '1 4'
# var2 = '1'
# var3 = '3 4 5 6'
# 4)var1 = '5 5'
# var2 = '10 20 30 40 50'
# var3 = '10 20 30 40 50'



# подставлял в эталонное решение
# var1 = '5 4' # количество элементов первого и второго множества
# var2 = '1 25 30 40 58 55 9'# элементы первого множества через пробел
# var3 = '11 20 30 1 50 24 78 9 1 ' # элементы второго множества через пробел

# эталонное решение

# mol = [int(x) for x in var1.split()] #строчки 72 - 74 по факту не нужны
# n = mol[0]
# m = mol[1]
# set_1 = set()
# set_2 = set()
# list_1 = list()
# a = [int(x) for x in var2.split()]
# k = set(a)
# for i in k:
#    set_1.add(i)
# b = [int(x) for x in var3.split()]
# k1 = set(b)
# for i in k1:
#    set_2.add(i)
# lok = set_1 & set_2
# kool = list(lok)
# kool.sort()
# for i in kool:
#    print(i, end=' ')





        
    