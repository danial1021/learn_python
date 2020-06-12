from urllib.request import urlopen
from selenium import webdriver as wb
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np

url = "http://www.lotteria.com/menu/Menu_All.asp"
driver = wb.Chrome()
driver.get(url)

html = driver.page_source #chrome driver를 이용하여 html요청
soup = bs(html, 'html.parser') #html에 들어있는 값을 파싱하고 저장

menu_list = []
kcal_list = []
price_list = []

#select_one, select, find, find_all 4가지 연산자 중 선택하여 사용하면 됩니다.
menu = soup.select('ul > li > div.bx_flex.menuRoundWrap > div > a')
kcal = soup.select('div.bx_flex.menuRoundWrap > div > span')
price = soup.select('div.bx_flex.menuRoundWrap > div > strong')

for i in range(len(menu)):
    menu_list.append(menu[i].text)
    kcal_list.append(kcal[i].text[:-4])
    price_list.append(price[i].text[:-1])

dic = {'menu':menu_list, 'kcal':kcal_list, 'price':price_list} #이 부분 채우기
data = pd.DataFrame(dic) #이 부분 채우기

data.head()
#5줄만 출력하기

data.to_csv('./롯데리아메뉴.csv', index=False)#test 폴더에 csv파일로 저장

df= pd.read_csv('./롯데리아메뉴.csv', thousands=',')#이 부분 채우기

df.head()
#5줄만 출력하기

df.info() #df의 총 데이터 건수, 데이터 타입, Null 건수를 한 번에 알아보기

df.rename(columns = {'menu' : '메뉴'}, inplace = True) #df의 'menu' 칼럼명을 '메뉴'로 수정하기
print(df)

df.loc[81] = ['오미자에이드', 140, 3000]# 맨 마지막 그 다음 행(81번째 행)에 '메뉴'는 '오미자에이드', 'kcal'는 140, 'price'는 3000 정보를 가진 행 추가하기
df.tail(1)# 맨 마지막 행 확인하기

df2= df.copy()
df2['만족도']=np.nan
df2.head()

g_index = df[(df['kcal']<500)&(df['price']<=5000)].index
for i in g_index:
    df2.loc[i, '만족도']=5

s_index = df[(df['kcal']>=500)&(df['price']<1000)].index
for i in s_index:
    df2.loc[i, '만족도']=3# 인덱스가 s_index인 '만족도' 값을 모두 3로 만들기 (loc, iloc 명령 중 선택하여 사용)

b_index = df[df['kcal']>=1000].index
for i in b_index:
    df2.loc[i, '만족도']=1

df2.isna().sum()
df2[df2['만족도'].isnull()]
df2 = df2.dropna()
df2.isna().sum()

high_price = pd.DataFrame(df.sort_values(by='price', ascending=False))#이 부분 채우기 sort_values 함수 이용
high_price = high_price.set_index("메뉴")#이 부분 채우기 set_index 함수 이용 
high_price.head(7)

import matplotlib.pyplot as plt
%matplotlib inline

import platform
from matplotlib import font_manager, rc

plt.rcParams['axes.unicode_minus'] = False

#윈도우
path = "c:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=path).get_name()
rc('font', family=font_name)

#맥
#rc('font', family='AppleGothic')

plt.figure(figsize=(10,10))
plt.scatter(df['kcal'], df['price'], s=50, c='g', marker='*')
plt.title('롯데리아 메뉴') #제목
plt.xlabel('칼로리') #x축 제목
plt.ylabel('가격') #y축 제목
plt.ylim(0, 20000) #y축 범위4

for i in range(7):
    plt.text(high_price['kcal'][i], high_price['price'][i], high_price.index[i])
plt.savefig('롯데리아메뉴.png')