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
'Aaz': ("спички", "спальник", "дрова", "топор",'кружка',"фонарь","удочка"),
'Skeeve': ("спальник", "спички", "вода", "еда", 'ружье',"фонарь"),
'Tananda': ("вода", "спички", "косметичка",'нож','кружка',"фонарь","сапоги","удочка"),
'John': ("газовая горелка", "чай","кружка","спальник","спички","фонарь","удочка"),
'Mary': ( "палатка", "спички", "спальник","кружка","фонарь","удочка")
}

all_unic_elements=set()
for k,v in hike.items(): # находим множетсво всех уникальных вещей среди наборов у друзей
    if all_unic_elements!=set(): 
        all_unic_elements = all_unic_elements.union(set(v))
    else:
        all_unic_elements=set(v) 
print(f'all_unic_elements:\n{all_unic_elements}')

all_unic_elements_dict = {} # создадим словарь вещей и будем в него заносить значения - всех, у кого есть данная вещь
for k,v in hike.items():
    for i in v:
        all_unic_elements_dict[i]=all_unic_elements_dict.get(i,[])+[k]
print(f'all_unic_elements_dict:\n{all_unic_elements_dict}')

common_things = []  #список вещей, встречающихся у каждого
unic_things=dict()  # словарь вещей, встречающихся у кого-то одного
persons_who_not_have_common_things=dict() # словарь вещей, которые есть у каждого, кроме одного члена группы
hike_mens_name_list = [i for i in hike]
#print(hike_mens_name_list)
for k,v in all_unic_elements_dict.items():
    if len(v)==len(hike_mens_name_list):
        common_things.append(k)
    if len(v)==1:
        unic_things[k]=v
    if len(v)==len(hike_mens_name_list)-1:
        persons_who_not_have_common_things[k]=set(hike_mens_name_list).difference(set(v))
print(f'common_things:\n{common_things}')
print(f'unic_things:\n{unic_things}')
print(f'persons_who_not_have_common_things:\n{persons_who_not_have_common_things}')



