# Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.

# Пример:


# list_1 = [1, 2, 3, 4, 5]
# k = 6
# # 5

list_1 = [-4, 1, 2, 3, -2, 4, 5, -1, 4, 8, 7]
k = -6
near_k = list_1[0]
diff = abs(k - near_k)
for i in range(1,len(list_1)):
    if abs(k-list_1[i])<diff:
        near_k = list_1[i]
        diff = abs(k - near_k)
    elif abs(k-list_1[i])==diff:
        if list_1[i]>near_k:
            near_k = list_1[i]
            diff = abs(k - near_k)
    #print(diff)
print(near_k) 

# Что подставлял автотест:

# 1) # list_1 = [1, 2, 3, 4, 5]
# # k = 6
# 2)list_1 = [2, 4, 1, 6, 8, 2, 9, 3, 2, 5]
# k = 10
# 3)list_1 = [1, 4, 3, 7, 8, 9, 2]
# k = 8
# 4)list_1 = [1, 12, 6, 7, 8, 15]
# k = 11
