# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума).
# На вход подается список с элементамиlist_1 и границы диапазона в виде чисел min_number, max_number.

# Пример

# На входе:


# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = 0
# max_number = 10
# На выходе:


# 1
# 2
# 3
# 6
# 7
# 9
# 10
# 11
# 13
# 14
# 16
# 19

list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = 0
max_number = 10

def Find_indexes_of_nums_belong_number_line(nums_list, min_num, max_num):
    number_line=list(range(min_num,max_num+1))
    # print(number_line)
    for i in range(len(nums_list)):
        if nums_list[i] in number_line:
            print(i)
Find_indexes_of_nums_belong_number_line(list_1,min_number,max_number)