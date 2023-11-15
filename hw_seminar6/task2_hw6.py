# Заполните массив элементами арифметической прогрессии. Её первый элемент a1 , разность d и количество элементов n будет задано автоматически. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.

# Пример

# На входе:


# a1 = 2
# d = 3
# n = 4
# На выходе:


# 2
# 5
# 8
# 11

# an = a1 + (n-1) * d.

a1 = 5
d = -1
n = 10

def Arithmetical_progression_print_n_members(m1, ar_diff, n_members):
    for i in range(1,n_members+1):
        print(m1+(i-1)*ar_diff)
Arithmetical_progression_print_n_members(a1,d,n)