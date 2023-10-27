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
'Aaz': ("спички", "спальник", "дрова", "топор",'кружка',"фонарь"),
'Skeeve': ("спальник", "спички", "вода", "еда", 'ружье',"фонарь"),
'Tananda': ("вода", "спички", "косметичка",'нож','кружка',"фонарь"),
'John': ("газовая горелка", "чай","кружка","спальник","спички","фонарь"),
'Mary': ( "палатка", "спички", "спальник","кружка","фонарь")
}
all_unic_elements=set() # множетсво всех уникальных вещей среди наборов у друзей
common_things=set() #эти вещи встречаются у каждого
unic_things=dict() #эти вещи встречаются только у кого-то одного
persons_who_not_have_common_things=dict() #люди, у которых нет какой-либо вещи, которая встречается у всех

for k,v in hike.items(): # находим множетсво всех уникальных вещей среди наборов у друзей
    if all_unic_elements!=set(): 
        all_unic_elements = all_unic_elements.union(set(v))
    else:
        all_unic_elements=set(v) 
print(f'all_unic_elements:\n{all_unic_elements}')

for i in hike: #Находим вещи, встречающиеся у каждого
    if common_things!=set(): 
        common_things = common_things.intersection(set(hike[i]))
    else:
        common_things=set(hike[i])  
print(f'common_things:\n{common_things}')


for i in hike:   # находим вещи, встречающиеся только у кого-то одного 
    curr_set=set(hike[i])
    for j in hike:
        if j!=i:
            curr_set=curr_set.difference(set(hike[j]))
    if curr_set!=set():
        unic_things[tuple(curr_set)]=i
print(f'unic_things:\n{unic_things}')

for i in hike:  # находим вещи, которые есть у каждого, кроме одного члена группы
    curr_set = set()
    for j in hike:
        if i!=j:
            if curr_set!=set(): 
                curr_set = curr_set.intersection(set(hike[j]))
            else:
                curr_set=set(hike[j])
    if curr_set.difference(set(hike[i]))!=set():
        persons_who_not_have_common_things[tuple(curr_set.difference(set(hike[i])))]=i
print(f'persons_who_not_have_common_things:\n{persons_who_not_have_common_things}')
