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
lst1 = list(data['whoAmI'])
lst_human = []
lst_robot = []
for i in data['whoAmI']:
    lst_human.append(i=='human')
    lst_robot.append(i=='robot')
hot_data = pd.DataFrame({'human':lst_human,'robot':lst_robot})
print(hot_data)
