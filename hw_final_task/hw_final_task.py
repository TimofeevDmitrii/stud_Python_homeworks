# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

# Статья про one hot вид https://colab.research.google.com/drive/1qKamnDiRmpRZkpiqWPkunBdAhmzhMcGz?usp=sharing

import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
pd.get_dummies(data['whoAmI'])
# print(data.head()) 
# print(pd.get_dummies(data['whoAmI']))


# Ссылка на решение данной задачи в colab (последняя строка с кодом) https://colab.research.google.com/drive/1NzekPM2afVqmeoEXKzVsN21yIvQ9_Hp4


#Решение без get_dummies
set_data_val = set(data['whoAmI'])
hot_data_dict = {}
for k in set_data_val:
    hot_data_dict[k]=[]
# print(hot_data_dict)
for i in data['whoAmI']:
    for key in hot_data_dict:
       hot_data_dict[key].append(key==i)                
hot_data = pd.DataFrame(hot_data_dict)
print(hot_data)


# Другой вариант решения без get_dummies 
# import pandas as pd
# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()
# print(f"{data} \n")
# unique_values = data['whoAmI'].unique()
# for value in unique_values:
#     data[value] = (data['whoAmI'] == value).astype(int)
# data.drop('whoAmI', axis=1, inplace=True)
# data.head()
# print(data)
