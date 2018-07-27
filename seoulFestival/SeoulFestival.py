import pandas as pd
import os
import matplotlib.pyplot as plt


flowlist = os.listdir('C:\\deep\\seoulFestival\\flowdata')
flow_nm = [file_name[:-8] for file_name in flowlist]

flow_dict = {}
flow_path = 'C:\\deep\\seoulFestival\\flowdata\\'

for i in range(len(flowlist)):
    # flow_nm[i] = pd.read_csv(a + flowlist[i], encoding="cp949", sep='\t', dtype=str, index_col=0)
    flow_dict[flow_nm[i]] = pd.read_csv(flow_path + flowlist[i], encoding="cp949", sep='\t', index_col=None)

revlist = os.listdir('C:\\deep\\seoulFestival\\revenuedata')
rev_nm = [file_name[:-15] for file_name in revlist]
rev_dict = {}
rev_path = 'C:\\deep\\seoulFestival\\revenuedata\\'

for j in range(len(rev_nm)):
    df = pd.read_csv(rev_path + revlist[j], encoding="cp949", sep='\t', index_col=None)
    df['Event'] = [rev_nm[j][:-10] for i in range(len(df.SECTOR))]
    rev_dict[rev_nm[j]] = df
# print(rev_dict[rev_nm[0]].head())
# for i in range(len(flowlist)):
#     print(flow_nm[i], "  ->", flow_dict[flow_nm[i]].shape)
# print("------------------------------------------------------------")
# for j in range(len(revlist)):
#     print(rev_nm[j], "  ->", rev_dict[rev_nm[j]].shape)

# print(flow_dict[flow_nm[0]].columns)
"""
# 리스트 item 중 특정값을 갖는 item들을 다시 리스트로 만들기 
flow_age_idx = []
for s in flow_nm:
    if "AGE" in s:
        flow_age_idx.append(s)
"""
# 좀 더 간단한 표현
flow_nm_age = [s for s in flow_nm if "AGE" in s]
flow_nm_time = [s for s in flow_nm if "TIME" in s]
# print(len(flow_nm_age))
# print(len(flow_nm_time))

flow_nm_age_dict = {}
for key in flow_nm_age:
    flow_nm_age_dict[key] = flow_dict.get(key)
# print(type(flow_nm_age_dict))
# print(flow_nm_age_dict[flow_nm_age[0]].columns)
flow_nm_time_dict = {}
for key in flow_nm_time:
    flow_nm_time_dict[key] = flow_dict.get(key)

# 연령대별 유동인구, 시간대별 유동인구 현황의 변수명을 비교
# for s in range(len(flow_nm_age)):
#     print(flow_nm_age[s], flow_nm_age_dict[flow_nm_age[s]].columns)

# print('---------------------------------------------------------------------------')
# for s in range(len(flow_nm_time)):
#     print(flow_nm_time[s], flow_nm_time_dict[flow_nm_time[s]].columns)
"""
    1)EVENT : 축제명 코드
    – LAMP : 서울 빛초롱 축제 
    – CULTURE : 서울 문화의 밤 
    – DRUM : 서울 드럼 페스티벌 
    – HISEOUL : 하이서울페스티벌 
    – KIMJANG : 서울 김장문화제
    2) SECTOR : 축제 대상 지역을 섹터로 나누어 구분한 번호
    3) DATE : 유동인구를 추출한 날짜
    4) INFLOW_CD : 축제 방문객의 거주지역 코드 (이곳에서 축제를 방문했다는 의미)
    5) INFLOW_NM : 축제 방문객의 거주지역명(1: 특별시/도 구분, 2:거주지 구명)
    6) SUM : 연령대별 유동인구의 총합
    7) SUM_M : 연령대별 남성 유동인구의 합
    8) SUM_F : 연령대별 여성 유동인구의 합
    9) M_0004 : 남성(Male) 0 세 ~ 5 세미만 유동인구 수
    10) M_0509 : 남성(Male) 5 세 ~ 10 세미만 유동인구 수
    11) M_1014 : 끝의 4 자리 숫자를 연령대로 해석하여 활용. (기타 변수 설명 생략)
    12) M_70U : 남성(Male) 70 세 이상 유동인구 수
    13) F_0004 : 여성(Female) 0 세 ~ 5 세미만 유동인구 수
    14) F_0509 : 여성(Female) 5 세 ~ 10 세미만 유동인구 수
    15) F_1014 : 끝의 4 자리 숫자를 연령대로 해석하여 활용. (기타 변수 설명 생략)
    16) F_70U : 여성(Female) 70 세 이상 유동인구 수
"""

# DRUM의 시간대별의 경우 2015년 데이터에 EVENT 명과 SECTOR 번호가 생략되어 있으므로 시간대별 유동인구 분석에서 제외
# delete_word = 'DRUM_TIME_INFLOW_2014', 'DRUM_TIME_INFLOW_2015'
# flow_nm_time2 = flow_nm_time.remove(delete_word)
# ValueError: list.remove(x): x not in list
flow_nm_time2 = [e for e in flow_nm_time if e not in ('DRUM_TIME_INFLOW_2014', 'DRUM_TIME_INFLOW_2015')]

# print('---------------------------------------------------------------------------')
flow_nm_time2_dict = {}
for key in flow_nm_time2:
    flow_nm_time2_dict[key] = flow_nm_time_dict.get(key)
# for s in range(len(flow_nm_time2)):
#     print(flow_nm_time2[s], " -> ", flow_nm_time2_dict[flow_nm_time2[s]].columns)

# 각각의 데이터프레임의 컬럼 동일화
for s in range(len(flow_nm_time2)):
    flow_nm_time2_dict[flow_nm_time2[s]].columns = \
        ['EVENT', 'SECTOR', 'DATE', 'INFLOW_CD', 'INFLOW_NM', 'SUM',
         'TIME_0', 'TIME_1', 'TIME_2', 'TIME_3', 'TIME_4', 'TIME_5',
         'TIME_6', 'TIME_7', 'TIME_8', 'TIME_9', 'TIME_10', 'TIME_11',
         'TIME_12', 'TIME_13', 'TIME_14', 'TIME_15', 'TIME_16', 'TIME_17',
         'TIME_18', 'TIME_19', 'TIME_20', 'TIME_21', 'TIME_22', 'TIME_23']
# for s in range(len(rev_nm)):
#     print(rev_nm[s], " -> ", rev_dict[rev_nm[s]].columns)


plt.rcParams['axes.unicode_minus'] = False
# print(rev_dict['LAMP_CARD_2015']['DATE'])

tmp = rev_dict['HISEOUL_CARD_2014']['DATE'].astype(str)
# print(type(tmp))
hi_year14, hi_month14, hi_day14 =[], [], []

for i in range(len(tmp)):
    a = tmp[i]
    hi_year14.append(a[:4])
    hi_month14.append(a[4:6])
    hi_day14.append(a[6:])
rev_dict['HISEOUL_CARD_2014']['hi_year14'] = hi_year14
rev_dict['HISEOUL_CARD_2014']['hi_month14'] = hi_month14
rev_dict['HISEOUL_CARD_2014']['hi_day14'] = hi_day14
# print(rev_dict['HISEOUL_CARD_2014'].head())

tmp = rev_dict['HISEOUL_CARD_2015']['DATE'].astype(str)
hi_year15, hi_month15, hi_day15 = [],[],[]
for i in range(len(tmp)):
    a = tmp[i]
    hi_year15.append(a[:4])
    hi_month15.append(a[4:6])
    hi_day15.append(a[6:])
rev_dict['HISEOUL_CARD_2015']['hi_year15'] = hi_year15
rev_dict['HISEOUL_CARD_2015']['hi_month15'] = hi_month15
rev_dict['HISEOUL_CARD_2015']['hi_day15'] = hi_day15

hiseoul2014 = pd.DataFrame(rev_dict['HISEOUL_CARD_2014']
                           [['DATE','SEX','TIME','MONEY','hi_year14', 'hi_month14', 'hi_day14']])
hiseoul2015 = pd.DataFrame(rev_dict['HISEOUL_CARD_2015']
                           [['DATE','SEX','TIME','MONEY','hi_year15', 'hi_month15', 'hi_day15']])
# print(hiseoul2014.head())
# print(hiseoul2015.head())
# x = rev_dict['HISEOUL_CARD_2014'].TIME
# y = rev_dict['HISEOUL_CARD_2014'].MONEY
# plt.plot(x, y)
# plt.show()

print(hiseoul2015['TIME'].unique())
a = hiseoul2015.groupby(['TIME']).sum()['MONEY']
b = hiseoul2015.groupby(['hi_month15']).sum()['MONEY']
plt.table(a,b)
plt.show()
