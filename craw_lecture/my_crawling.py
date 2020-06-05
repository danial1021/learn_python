from selenium import webdriver as wb
import time

driver = wb.Chrome()

url = 'https://www.hsd.co.kr/menu/menu_list'
driver.get(url)

for i in range(3):
    driver.find_element_by_xpath('//*[@id="btn_more"]/span/a').click()
    time.sleep(3)