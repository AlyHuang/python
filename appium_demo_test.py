#!/usr/bin/python
#-*-coding:utf-8-*-
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0.1'
desired_caps['deviceName'] = 'bc5c8261'
desired_caps['appPackage'] = 'com.miui.calculator'
desired_caps['appActivity'] = '.cal.CalculatorActivity'

driver = webdriver.Remote('http://localhost:4725/wd/hub', desired_caps)

driver.find_element_by_name("1").click()

driver.find_element_by_name("5").click()

driver.find_element_by_name("9").click()

driver.find_element_by_id("del").click()

driver.find_element_by_name("9").click()

driver.find_element_by_name("5").click()

driver.find_element_by_id("plus").click()

driver.find_element_by_name("6").click()

driver.find_element_by_id("equal").click()

driver.quit()