'''
Задача VERY HARD необязательная
Имеется список случайных целых чисел. Создайте список, в который попадают числа, описывающие максимальную сплошную возрастающую последовательность. Порядок элементов менять нельзя.
Одно число - это не последовательность.

Пример:

[1, 5, 2, 3, 4, 6, 1, 7] => [1, 7] так как здесь вразброс присутствуют все числа от 1 до 7

[1, 5, 2, 3, 4, 1, 7, 8 , 15 , 1 ] => [1, 5] так как здесь есть числа от 1 до 5 и эта последовательность длиннее чем от 7 до 8

[1, 5, 3, 4, 1, 7, 8 , 15 , 1 ] => [3, 5] так как здесь есть числа от 3 до 5 и эта последовательность длиннее чем от 7 до 8

[1, 3, 6, 8, 11, 14]

[-1, 0, 2, 8, 0, 1, -2]
'''


array = [1, 5, 2, 3, 4, 6, 1, 7]
nmin = array[0]
nmax = array[0]
for i in array:
    n=i+1
    j=0
    while (j<=len(array)-1):
    #for j in range(len(array)-1): с циклом for такое не прокатит =)
        if n==array[j]:
            n = n+1
            j=0
        else:
            j+=1
    #print(f"[{i};{n-1}]")
    if (n-i>nmax-nmin+1): # if ((n-1)-i+1>nmax-nmin+1):
        nmin = i
        nmax = n-1
if(nmax-nmin+1 != 1):
    print(f"[{nmin};{nmax}]")
else:
    print("Сплошной возрастающей последовательности во входном ряде чисел найти не удалось")
        
        
        
