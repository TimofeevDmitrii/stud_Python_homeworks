# доп задача, НЕ дз.
# Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников. Теперь он использует их в качестве серверов "Пегого дудочника". Помогите владельцу фирмы отыскать все зараженные холодильники.
# ​
# Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр, и если в ней присутствует слово "anton" (необязательно рядом стоящие буквы, главное наличие последовательности букв), то холодильник заражен и нужно вывести номер холодильника, нумерация начинается с единицы
# ​
# Формат входных данных
# В первой строке подаётся число
# n
# n – количество холодильников. В последующих n строках вводятся строки, содержащие латинские строчные буквы и цифры, в каждой строке от 5 до 100 символов.
# ​
# Sample Input 1:
# 6
# 222anton456
# a1n1t1o1n1
# 0000a0000n00t00000o000000n
# gylfole
# richard
# ant0n
# Sample Output 1:
# 1 2 3
# Sample Input 2:
# 9
# osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen
# anton
# aoooooooooontooooo
# elelelelelelelelelel
# ntoneeee
# tonee
# 253235235a5323352n25235352t253523523235oo235523523523n
# antoooooooooooooooooooooooooooooooooooooooooooooooooooon
# unton
# Sample Output 2:
# 1 2 7 8



input_mess='''9
osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen
anton
aoooooooooontooooo
elelelelelelelelelel
ntoneeee
tonee
253235235a5323352n25235352t253523523235oo235523523523n
antoooooooooooooooooooooooooooooooooooooooooooooooooooon
unton'''


# input_mess='''6
# 222anton456
# a1n1t1o1n1
# 0000a0000n00t00000o000000n
# gylfole
# richard
# ant0n'''

list_1 = input_mess.split('\n')
#print(list_1)
hazard_word = ''
infection_word = 'anton'
infection_list = []
for i in range(1,len(list_1)):
    n=0
    temp_k=0
    count=0
    while count<len(list_1[i]) and n<len(infection_word):
        for k in range(temp_k,len(list_1[i])):
            if list_1[i][k]==infection_word[n]:
                hazard_word+=list_1[i][k]
                temp_k=k+1
                n+=1
                count+=1
                break  
            count+=1 
    if hazard_word=='anton':
        infection_list.append(i)
    hazard_word = ''
for i in infection_list:
    print(i, end=' ')
