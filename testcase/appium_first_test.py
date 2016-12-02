#!/usr/bin/python
#-*-coding:utf-8-*-
from appium import webdriver

desired_capabilities = {}
desired_capabilities['platformName'] = 'Android'
desired_capabilities['platformVersion'] = '5.1.1'
desired_capabilities['deviceName'] = 'NHG6T16506000967'
desired_capabilities['appPackage'] = 'com.android.calculator2'
desired_capabilities['appActivity'] = '.Calculator'


if __name__ == '__main__':
	driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)

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