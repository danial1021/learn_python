from selenium import webdriver as wb
from bs4 import BeautifulSoup as bs
import time
import pandas as pd

url = 'http://www.istarbucks.co.kr/store/store_map.do'

driver = wb.Chrome()
driver.get(url)

#지역검색 버튼 클릭
btn_search = driver.find_element_by_class_name('loca_search')
btn_search.click()

#광주지역 클릭
li = driver.find_elements_by_css_selector('ul.sido_arae_box > li')
li[2].click()

#광주지역에서 전체지역 클릭
allArea = driver.find_element_by_css_selector('ul.gugun_arae_box > li')
allArea.click()

soup = bs(driver.page_source,'html.parser')

#지점명, 주소, 번호 수집
name_list = []
addr_list = []
tel_list = []

# names = soup.select('li.quickResultLstCon > strong')
names = soup.select('#mCSB_3_container > .quickSearchResultBoxSidoGugun > li > strong')
# addrs = soup.findAll('p',class_='result_details')
addrs = soup.select('#mCSB_3_container > .quickSearchResultBoxSidoGugun > li > strong + p')
print(len(names), len(addrs))

for index in range(len(names)):
    name_list.append(names[index].text)
    addr_list.append(addrs[index].text[:-9])
    tel_list.append(addrs[index].text[-9:])

dic = {'name':name_list, 'address':addr_list, 'tel':tel_list}
df = pd.DataFrame(dic)
df.head()

df.to_csv("200604 스타벅스 매장 정보.csv")