from bs4 import BeautifulSoup
import requests
import lxml
from selenium import webdriver
import time



chrdir = "./chromedriver.exe"
driver = webdriver.Chrome(chrdir)
driver.get("https://eduro.gen.go.kr/hcheck/index.jsp%22)
driver.find_element_by_xpath('//[@id="container"]/div/div/div/div[2]/div/a[2]/div').click()
driver.find_element_by_xpath('//[@id="schulNm"]').click()
time.sleep(3)
driver.find_element_by_name("schulNm").send_keys("소프트")
driver.find_element_by_xpath('//[@id="btnSrchSchul"]').click()
driver.find_element_by_name("pName").send_keys("") #이름
driver.find_element_by_name("frnoRidno").send_keys("") #생년월일
driver.find_element_by_xpath('//[@id="btnConfirm"]').click()
time.sleep(2)
driver.find_element_by_xpath('//[@id="infoForm"]/div/div/table[1]/tbody/tr[2]/td/span/label[1]').click()
driver.find_element_by_xpath('//[@id="infoForm"]/div/div/table[2]/tbody/tr[2]/td/span/label[1]').click()
driver.find_element_by_xpath('//[@id="infoForm"]/div/div/table[3]/tbody/tr[2]/td/span/label[1]').click()
driver.find_element_by_xpath('//[@id="infoForm"]/div/div/table[4]/tbody/tr[2]/td/span/label[1]').click()
driver.find_element_by_xpath('//[@id="infoForm"]/div/div/table[5]/tbody/tr[2]/td/span/label[1]').click()
driver.find_element_by_xpath('//[@id="btnConfirm"]').click()
time.sleep(3)
driver.quit()
