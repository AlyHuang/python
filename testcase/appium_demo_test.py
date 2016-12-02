#!/usr/bin/python
#-*-coding:utf-8-*-
import unittest
from selenium import webdriver
from appium import webdriver
import time

class UnitTestLogin(unittest.TestCase):
    def setUp(self):
        desired_capabilities = {}
        desired_capabilities['platformName'] = 'Android'
        desired_capabilities['platformVersion'] = '4.4.4'
        desired_capabilities['deviceName'] = 'c23a016'
        desired_capabilities['appPackage'] = 'com.htmm.owner'
        desired_capabilities['appActivity'] = '.activity.main.SplashActivity'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities)

    def tearDown(self):
        self.driver.close_app()
        self.driver.quit()

    def test_Login(self):
        time.sleep(2)
        self.driver.network_connection
        Account_text=self.driver.find_element_by_id("et_account")
        print (Account_text)
        Account_text.send_keys("18318704565")
        Password_text=driver.find_element_by_id("et_pwd").click()
        Password_text.send_keys("707017")
        driver.find_element_by_id("btn_login").click()


if __name__ == '__main__':    
    suite = unittest.TestLoader().loadTestsFromTestCase(UnitTestLogin)
    unittest.TextTestRunner(verbosity=2).run(suite)