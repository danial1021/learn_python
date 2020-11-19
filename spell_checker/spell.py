# coding=utf-8

import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys

fp = open("1.txt", 'r', encoding="utf-8")
text = fp.read()
fp.close()

ready_list = []

while (len(text) > 500):
  temp_str = text[:500]
  last_space = temp_str.rfind(' ')
  temp_str = text[0:last_space]
  ready_list.append(temp_str)

  text = text[last_space:]

ready_list.append(text)
# print(ready_list)

driver = webdriver.Chrome('./chromedriver')
driver.get("http://www.naver.com")

elem = driver.find_element_by_id("query")
elem.send_keys("맞춤법 검사기")

elem = driver.find_element_by_id("search_btn")
elem.click()

time.sleep(2)
textarea = driver.find_element_by_class_name("txt_gray")

new_str = ''
for ready in ready_list:
  textarea.send_keys(Keys.CONTROL, 'a')
  textarea.send_keys(ready)

  elem = driver.find_element_by_class_name("btn_check")
  elem.click()

  time.sleep(2)
  soup = BeautifulSoup(driver.page_source, 'html.parser')
  string = soup.select("p._result_text.stand_txt")[0].text 
  new_str += string.replace('. ', '.\n')

fp = open("result.txt", 'w', encoding='utf-8')
fp.write(new_str)
fp.close()