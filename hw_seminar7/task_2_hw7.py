# Напишите функцию print_operation_table(operation, num_rows, num_columns), которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.

# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.

# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).

# Если строк меньше двух, выдайте текст
# ОШИБКА! Размерности таблицы должны быть больше 2!.

# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

# Пример

# На входе:

# print_operation_table(lambda x, y: x * y, 3, 3)

# На выходе:


# 1 2 3
# 2 4 6 
# 3 6 9

# Мой вариант решения
def print_operation_table(operation, num_rows, num_columns):
    if num_rows<2 or num_columns<2:
        print("ОШИБКА! Размерности таблицы должны быть больше 2!") # Правильнее было бы "больше либо равны 2"; но автотест принимает такой варинат по заданию
    else:
        for i in range(1,num_rows+1):
            res_list=[]
            for j in range(1,num_columns+1):
                if i==1 or j==1:
                    res_list.append(max([i,j]))
                else:
                    res_list.append(operation(i,j))
            print(*res_list)

print_operation_table(lambda x, y: x/y, 4, 4)     

# Эталонный вариант решения в автотесте
def print_operation_table(operation, num_rows, num_columns):
    if num_rows < 2 or num_columns < 2:
        print('ОШИБКА! Размерности таблицы должны быть больше 2!')
    else:
        header = ' '.join([str(i) for i in range(1, num_columns + 1)])
        print(header)
        for i in range(2, num_rows + 1):
            row = [str(i)] + [str(operation(i, j)) for j in range(2, num_columns + 1)]
            print(' '.join(row))



# # Автотесты
# Не все тесты пройдены, есть ошибки :(


# Количество затраченных попыток: 1

# Время выполнения: 1.320442 сек

# Общая статистика
# Всего тестов: 6. Пройдено: 2. Не пройдено: 4.

# Подробную информацию по каждому тесту смотрите ниже.

# Тест 1
# Тест не пройден ✗

# Формулировка:

# * Итоговый код для проверки. Иногда добавляем что-то от себя :)


# import warnings

# warnings.filterwarnings('ignore')

# # Введите ваше решение ниже
# def print_operation_table(operation, num_rows, num_columns):
#     if num_rows<3:
#         print("ОШИБКА! Размерности таблицы должны быть больше 2!")
#     else:
#         for i in range(1,num_rows+1):
#             for j in range(1,num_columns+1):
#                 print(operation(i,j), end=' ')
#             print()

# #При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

# #При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки

# # print_operation_table(lambda x, y: x * y, 3, 3) 

# print_operation_table(lambda x, y: x * y, 3, 3)


# Ожидаемый ответ:

# 1 2 3
# 2 4 6
# 3 6 9

# Ваш ответ:

# 1 2 3 
# 2 4 6 
# 3 6 9
# Тест 2
# Тест не пройден ✗

# Формулировка:

# * Итоговый код для проверки. Иногда добавляем что-то от себя :)


# import warnings

# warnings.filterwarnings('ignore')

# # Введите ваше решение ниже
# def print_operation_table(operation, num_rows, num_columns):
#     if num_rows<3:
#         print("ОШИБКА! Размерности таблицы должны быть больше 2!")
#     else:
#         for i in range(1,num_rows+1):
#             for j in range(1,num_columns+1):
#                 print(operation(i,j), end=' ')
#             print()

# #При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

# #При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки

# # print_operation_table(lambda x, y: x * y, 3, 3) 

# print_operation_table(lambda x, y: x + y, 4, 4)


# Ожидаемый ответ:

# 1 2 3 4
# 2 4 5 6
# 3 5 6 7
# 4 6 7 8

# Ваш ответ:

# 2 3 4 5 
# 3 4 5 6 
# 4 5 6 7 
# 5 6 7 8
# Тест 3
# Тест не пройден ✗

# Формулировка:

# * Итоговый код для проверки. Иногда добавляем что-то от себя :)


# import warnings

# warnings.filterwarnings('ignore')

# # Введите ваше решение ниже
# def print_operation_table(operation, num_rows, num_columns):
#     if num_rows<3:
#         print("ОШИБКА! Размерности таблицы должны быть больше 2!")
#     else:
#         for i in range(1,num_rows+1):
#             for j in range(1,num_columns+1):
#                 print(operation(i,j), end=' ')
#             print()

# #При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

# #При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки

# # print_operation_table(lambda x, y: x * y, 3, 3) 

# print_operation_table(lambda x, y: x - y, 5, 5)


# Ожидаемый ответ:

# 1 2 3 4 5
# 2 0 -1 -2 -3
# 3 1 0 -1 -2
# 4 2 1 0 -1
# 5 3 2 1 0

# Ваш ответ:

# 0 -1 -2 -3 -4 
# 1 0 -1 -2 -3 
# 2 1 0 -1 -2 
# 3 2 1 0 -1 
# 4 3 2 1 0
# Тест 4
# Тест пройден успешно ✓

# Формулировка:

# * Итоговый код для проверки. Иногда добавляем что-то от себя :)


# import warnings

# warnings.filterwarnings('ignore')

# # Введите ваше решение ниже
# def print_operation_table(operation, num_rows, num_columns):
#     if num_rows<3:
#         print("ОШИБКА! Размерности таблицы должны быть больше 2!")
#     else:
#         for i in range(1,num_rows+1):
#             for j in range(1,num_columns+1):
#                 print(operation(i,j), end=' ')
#             print()

# #При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

# #При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки

# # print_operation_table(lambda x, y: x * y, 3, 3) 

# print_operation_table(lambda x, y: x * y, 1, 2)
# Тест 5
# Тест не пройден ✗

# Формулировка:

# * Итоговый код для проверки. Иногда добавляем что-то от себя :)


# import warnings

# warnings.filterwarnings('ignore')

# # Введите ваше решение ниже
# def print_operation_table(operation, num_rows, num_columns):
#     if num_rows<3:
#         print("ОШИБКА! Размерности таблицы должны быть больше 2!")
#     else:
#         for i in range(1,num_rows+1):
#             for j in range(1,num_columns+1):
#                 print(operation(i,j), end=' ')
#             print()

# #При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

# #При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки

# # print_operation_table(lambda x, y: x * y, 3, 3) 

# print_operation_table(lambda x, y: x / y, 4, 4)


# Ожидаемый ответ:

# 1 2 3 4
# 2 1.0 0.6666666666666666 0.5
# 3 1.5 1.0 0.75
# 4 2.0 1.3333333333333333 1.0

# Ваш ответ:

# 1.0 0.5 0.3333333333333333 0.25 
# 2.0 1.0 0.6666666666666666 0.5 
# 3.0 1.5 1.0 0.75 
# 4.0 2.0 1.3333333333333333 1.0
# Тест 6
# Тест пройден успешно ✓

# Формулировка:

# * Итоговый код для проверки. Иногда добавляем что-то от себя :)


# import warnings

# warnings.filterwarnings('ignore')

# # Введите ваше решение ниже
# def print_operation_table(operation, num_rows, num_columns):
#     if num_rows<3:
#         print("ОШИБКА! Размерности таблицы должны быть больше 2!")
#     else:
#         for i in range(1,num_rows+1):
#             for j in range(1,num_columns+1):
#                 print(operation(i,j), end=' ')
#             print()

# #При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

# #При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки

# # print_operation_table(lambda x, y: x * y, 3, 3) 

# print_operation_table(lambda x, y: x * y)

