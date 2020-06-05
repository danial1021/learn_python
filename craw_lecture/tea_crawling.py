from selenium import webdriver as wb
import time
from bs4 import BeautifulSoup as bs
import pandas as pd

driver = wb.Chrome()

url = 'https://www.hsd.co.kr/menu/menu_list'
driver.get(url)

btn = driver.find_element_by_class_name("c_05")

for _ in range(3):
    btn.click()
    time.sleep(2)

soup = bs(driver.source_page, 'html.parser')
soup.select("")
    