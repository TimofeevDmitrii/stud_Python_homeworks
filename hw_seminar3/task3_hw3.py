# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.

# В случае с английским алфавитом очки распределяются так:

# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:

# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова k и выводит его. Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# Пример:


# k = 'ноутбук'
# # 12



# word = 'b'
# word = word.upper()
# if word in list3:
#     print('ok')

k = 'ноутбук'
k = k.upper()
value_dictkeys = [1, 2, 3, 4, 5, 8, 10]

list1 = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'] # 1 очко;
list2 = ['D', 'G'] # 2 очка;
list3 = ['B', 'C', 'M', 'P'] # 3 очка;
list4 = ['F', 'H', 'V', 'W', 'Y'] # 4 очка; 
list5 = ['K'] # 5 очков
list6 = ['J', 'X'] # 8 очков;
list7 = ['Q', 'Z'] # 10 очков.
eng_lists = [list1, list2, list3, list4, list5, list6, list7]
# eng_dict = {}
# for i in range(len(eng_lists)):
#     for n in eng_lists[i]:
#         eng_dict[n] = value_dictkeys[i]
# print(eng_dict)
list8 = ['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'] # 1 очко;
list9 = ['Д', 'К', 'Л', 'М', 'П', 'У'] # 2 очка;
list10 = ['Б', 'Г', 'Ё', 'Ь', 'Я'] # 3 очка;
list11 = ['Й', 'Ы'] # 4 очка; 
list12 = ['Ж', 'З', 'Х', 'Ц', 'Ч'] # 5 очков
list13 = ['Ш', 'Э', 'Ю'] # 8 очков;
list14 = ['Ф', 'Щ', 'Ъ'] # 10 очков.
rus_lists = [list8, list9, list10, list11, list12, list13, list14]    
# rus_dict = {}    
# for i in range(len(rus_lists)):
#     for n in rus_lists[i]:
#         rus_dict[n] = value_dictkeys[i]
# print(rus_dict)
scrabble_dict = {}
for i in (eng_lists, rus_lists):
    for n in range(len(i)):
        for j in i[n]:
            scrabble_dict[j] = value_dictkeys[n]
#print(scrabble_dict)
amount = 0
for m in k:
    amount += scrabble_dict[m]
print(amount)


# Эталонное решение
# points_en = {'AEIOULNSTR': 2 ,'DG':3, 'BCMP': 4,'y'=1, 'g'=4}

# word = input("input name ").upper()  # переводим все буквы в верхний регистр
# count = 0

# for i in word:
    
#     for j in points_en:
#         if i in j:
#             count = count + points_en[j]
  
# print(count)



# Другой вариант
# dict_Eng = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}
# dict_Rus = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}
# k = 'ноутбук'
# k = k.upper()  

# result = [key for letter in k for key, value in dict_Eng.items() if letter in value] or [key for letter in k for key, value in dict_Rus.items() if letter in value]
# print(sum(result))





