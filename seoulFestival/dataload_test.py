import os
import glob
import pandas as pd
import numpy as np

path_dir = 'C:\\deep\\seoulFestival\\flowdata'
flowlist = os.listdir(path_dir)
print(flowlist)

flow_nm = flowlist
for i in range(len(flowlist)):
    flow_nm[i] = flowlist[i][:-4]
print(flow_nm)

# flowlist = ro.r.dir("./flowdata/")

filepath = glob.glob('C:\\deep\\seoulFestival\\flowdata/*.txt')


filename = 'C:\\deep\\seoulFestival\\revenuedata/CULTURE_CARD_2014_215474_NEW.txt'
card_14 = pd.read_csv(filename, encoding='cp949', sep='\t', dtype=str, index_col=0)
print(card_14.head())

# [첫번째 방법] filename을 list로 가져온 후, list of dataframe으로 만들기
path = r'C:\\deep\\seoulFestival\\revenuedata'
allFiles = glob.glob(path + "/*.txt")   # list type
frame = pd.DataFrame()
list_data = []
for file_ in allFiles:  # file -> str type
    df = pd.read_csv(file_, encoding='cp949', sep='\t', dtype=str, index_col=0)
    list_data.append(df)

"""""""""""""""""""""""""""""""""""""""""""""
# [두번째 방법] 가져오는데 시간 더 오래 걸림
list_of_dfs = [pd.read_csv(filename, encoding='cp949', sep='\t', dtype=str, index_col=0)
               for filename in allFiles]
print(list_of_dfs[0].head())
"""""""""""""""""""""""""""""""""""""""""""""


print(type(list_data[0]))


