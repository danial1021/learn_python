from selenium import webdriver as wb
import time
from bs4 import BeautifulSoup as bs
import pandas as pd
# import numpy
# print(numpy.__version__)

driver = wb.Chrome()

url = 'https://www.hsd.co.kr/menu/menu_list'
driver.get(url)

btn = driver.find_element_by_class_name("c_05")

for _ in range(3):
    btn.click()
    time.sleep(2)


soup = bs(driver.source_page, 'html.parser')

name_list = []
name_tag_list = soup.select("h4.h.fz_03")
for name_tag in name_tag_list:
    name_list.append(name_tag.text)
print(name_list)

price_tag_list = soup.select("div.item-price > strong")
price_list = []
for price_tag in price_tag_list:
    price_list.append(price_tag.text)
print(price_list)
    
dic = {'name':name_list, 'price':price_list}
data = pd.DataFrame(dic)

data.to_csv("한솥.csv", index=False, encoding='euc-kr')
pd.read_csv("한솥.csv", encoding='euc-kr')