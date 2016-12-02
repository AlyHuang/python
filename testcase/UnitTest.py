#!/usr/bin/python
#-*-coding:utf-8-*-

from selenium import webdriver
from appium import webdriver
import unittest
import time
from Config import SetupConfig

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.driver=SetupConfig.SetupAppium();
        self.driver.network_connection

    def test_login(self):
        time.sleep(2)
        Account_text=self.driver.find_element_by_id("et_account")
        Account_text.send_keys("18318704565")
        Password_text=self.driver.find_element_by_id("et_pwd")
        Password_text.send_keys("707017")
        self.driver.find_element_by_id("btn_login").click()

    def tearDown(self):
        self.driver.close_app()
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(UnitTest)
    unittest.TextTestRunner(verbosity=2).run(suite)