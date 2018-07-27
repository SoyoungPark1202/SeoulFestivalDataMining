import os
import pandas as pd

list = os.listdir('C:\\deep\\seoulFestival\\flowdata')

name = [file_name[:-4] for file_name in list]

dict = {}

a = 'C:\\deep\\seoulFestival\\flowdata\\'

for i in range(len(list)):
    dict[name[i]] = pd.read_csv(a + list[i], encoding="cp949", sep='\t', dtype=str, index_col=0)

# print(dict[name[0]])

df = dict[name[0]]

print(df.head())