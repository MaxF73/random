# coding=<encoding name>
import pandas as pd 
import numpy as np 
import random
 
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print(data)
 
#==================================================#
data[1] = 1         #добавляем столбец
data.set_index([data.index, 'whoAmI'], inplace=True) #установим 'whoAmI' в качестве индекса
data = data.unstack(level=-1, fill_value = 0).astype(int)  
# переворачиваем фрейм данных, чтобы  меткми столбцов стали вместо меток строк
data.columns = data.columns.droplevel()
data.columns.name = None        #убираем заголовок 0 столбца
print(data)