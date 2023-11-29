# ДЗ
# 1 задача:

# Дан файл california_housing_train.csv. Определить среднюю стоимость дома , где количество людей от 0 до 500 (population) и сохранить ее в переменную avg.
# Используйте модуль pandas.

# import pandas as pd
# # Введите ваше решение ниже
# df = pd.read_csv('california_housing_train.csv')
# new_df=df.loc[(df['population']>=0) & (df['population']<=500),['median_house_value']]
# avg=new_df['median_house_value'].mean()
# print(avg)


# 2 задача:

# Дан файл california_housing_train.csv.
# Найти максимальное значение переменной "households" в зоне минимального значения переменной "population" и сохраните это значение в переменную max_households_in_min_population.
# Используйте модуль pandas.

# import pandas as pd
# df = pd.read_csv('california_housing_train.csv')   
# df_new=df.loc[df['population']==df['population'].min(),['households']]
# max_households_in_min_population=df_new['households'].max()
# print(max_households_in_min_population)