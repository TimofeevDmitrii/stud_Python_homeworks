# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# Example:
# 2 2
# 4

def Sum(a,b):
    if a==b==0:
        return 0
    else:
        res=0
        if a!=0:
            a-=1
            res+=1
        if b!=0:
            b-=1
            res+=1
        return res+Sum(a,b)   
    # else:                     # другой вариант 'else'(через цикл)
    #     list_var=[a,b]
    #     res=0
    #     for i in range(len(list_var)):
    #         if list_var[i]!=0:
    #             res+=1
    #             list_var[i]-=1
    #     return res+sum(list_var[0],list_var[1])
print(Sum(101,4))

# Доп. задача, которая напрашивается сама собой:
# Необходимо с помощью похожей рекурсивной функции (Из
# всех арифметических операций допускаются только +1 и -1) 
# сложить между собой N-ое количество неотрицательных чисел.
# Правда, без цикла тут не обойтись)))

# input_numbers = (1,3,60,10) # (1,3,60,10)
# def Sum(*args):
#     if set(args)=={0}:
#         return 0
#     elif set(args)==set():
#         return '' 
#     else:
#         list_var=list(args)
#         res=0
#         for i in range(len(list_var)):
#             if list_var[i]!=0:
#                 res+=1
#                 list_var[i]-=1
#         return res+Sum(*list_var)
# print(Sum(input_numbers))


# def test_fun(*params):  # определяем, что же такое в этом случае для функции params 
#     print(f'type_params is {type(params)}')
#     print(f'params={params}')
# test_fun(1, 4, 6)