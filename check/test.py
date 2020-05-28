#-*- coding:utf-8 -*-

from selenium import webdriver
import time

a = input("이름과 생년월일을 홍길동,123456 으로 넣어주세요 : ")
name = a.split(',')[0]
day = a.split(',')[1]

chrdir = "./chromedriver.exe"
driver = webdriver.Chrome(chrdir)
driver.get("https://eduro.gen.go.kr/hcheck/index.jsp")
driver.find_element_by_xpath('//*[@id="container"]/div/div/div/div[2]/div/a[2]/div').click()
driver.find_element_by_xpath('//*[@id="schulNm"]').click()
time.sleep(3)
driver.find_element_by_name("schulNm").send_keys("소프트") 
driver.find_element_by_xpath('//*[@id="btnSrchSchul"]').click()
driver.find_element_by_name("pName").send_keys(name) #자기 이름
driver.find_element_by_name("frnoRidno").send_keys(day) # 생년월일
driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="infoForm"]/div/div/table[1]/tbody/tr[2]/td/span/label[1]').click()
driver.find_element_by_xpath('//*[@id="infoForm"]/div/div/table[2]/tbody/tr[2]/td/span/label[1]').click()
driver.find_element_by_xpath('//*[@id="infoForm"]/div/div/table[3]/tbody/tr[2]/td/span/label[1]').click()
driver.find_element_by_xpath('//*[@id="infoForm"]/div/div/table[4]/tbody/tr[2]/td/span/label[1]').click()
driver.find_element_by_xpath('//*[@id="infoForm"]/div/div/table[5]/tbody/tr[2]/td/span/label[1]').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()
time.sleep(3)
driver.quit()
