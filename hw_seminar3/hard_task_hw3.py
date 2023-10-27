# ДОП задание

# Три друга взяли вещи в поход. Сформируйте словарь, где ключ - имя друга, а значение - кортеж вещей. Ответьте на вопросы:
# какие вещи взяли все три друга
# какие вещи уникальны, есть только у одного друга
# какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# Код должен расширяться на любое большее количество друзей.

# hike = {
# 'Aaz': ("спички", "спальник", "дрова", "топор"),
# 'Skeeve': ("спальник", "спички", "вода", "еда"),
# 'Tananda': ("вода", "спички", "косметичка"),
# }

hike = {
'Aaz': ("спички", "спальник", "дрова", "топор",'нож','кружка'),
'Skeeve': ("спальник", "спички", "вода", "еда", 'ружье'),
'Tananda': ("вода", "спички", "косметичка",'нож','кружка'),
}
all_unic_elements=set() # множетсво всех уникальных вещей среди наборов у друзей
common_things=set() #эти вещи встречаются у каждого
unic_things=dict() #эти вещи встречаются только у кого-то одного
mans_not_have_common_thing=dict() #люди, у которых нет какой-либо вещи, которая встречается у всех

for k,v in hike.items(): # находим множетсво всех уникальных вещей среди наборов у друзей
    for i in v:
        all_unic_elements.add(i)
print(f'all_unic_elements:\n{all_unic_elements}')

# all_unic_elements_dict = {} # создадим словарь вещей и будем в него заносить значения - у кого есть данная вещь
# for i in all_unic_elements:
#     all_unic_elements_dict[i]=''
# print(f'all_unic_elements_dict\n{all_unic_elements_dict}')

for i in hike: #Находим вещи, встречающиеся у каждого
    if common_things!=set(): 
        curr_set = set(hike[i])
        common_things = common_things.intersection(curr_set)
    else:
        for k in hike[i]:
            common_things.add(k)  
print(f'common_things:\n{common_things}')


for i in hike:   # находим вещи, встречающиеся только у кого-то одного 
    curr_set=set(hike[i])
    for j in hike:
        if j!=i:
            curr_set=curr_set.difference(set(hike[j]))
    if curr_set!=set():
        unic_things[tuple(curr_set)]=i
print(f'unic_things:\n{unic_things}')

for i in hike:
    curr_set = set()
    for j in hike:
        if i!=j:
            if curr_set!=set(): 
                curr_set = curr_set.intersection(set(hike[j]))
            else:
                for k in hike[j]:
                    curr_set.add(k)
    if curr_set.difference(set(hike[i]))!=set():
        mans_not_have_common_thing[tuple(curr_set.difference(set(hike[i])))]=i
print(f'mans_not_have_common_thing:\n{mans_not_have_common_thing}')
