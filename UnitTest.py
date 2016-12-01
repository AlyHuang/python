#!/usr/bin/python
#-*-coding:utf-8-*-

from selenium import webdriver
from appium import webdriver
import unittest



class UnitTest(unittest.TestCase):
    def setUp(self):
        desired_capabilities = {}
        desired_capabilities['platformName'] = 'Android'
        desired_capabilities['platformVersion'] = '5.1.1'
        desired_capabilities['deviceName'] = 'NHG6T16506000967'
        desired_capabilities['appPackage'] = 'com.android.calculator2'
        desired_capabilities['appActivity'] = '.Calculator'
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities)

    def tearDown(self):
        self.driver.quit()

    def test_test(self):
        sleep(5)
        driver.find.element.by.name("1").click()
        driver.find_element_by_name("5").click()
        driver.find_element_by_name("9").click()
        driver.find_element_by_id("del").click()
        driver.find_element_by_name("9").click()
        driver.find_element_by_name("5").click()
        driver.find_element_by_id("plus").click()
        driver.find_element_by_name("6").click()
        driver.find_element_by_id("equal").click()


if __name__ == '__main__':    
    unittest.main()
