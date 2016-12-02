#!/usr/bin/python
#-*-coding:utf-8-*-

import time
import unittest
import HTMLTestRunner
from appium import webdriver
from selenium import webdriver
from Config import SetupConfig


class UnitTestSuite(unittest.TestCase):
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
        
    def test_Enter(self):
        self.driver.start_activity('com.htmm.owner', '.activity.main.MainActivity')
        self.driver.find_element_by_name("小区广播").click()

    def tearDown(self):
        #self.driver.close_app()
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(UnitTestSuite('test_login'))
    suite.addTest(UnitTestSuite('test_Enter'))
    #unittest.TextTestRunner(verbosity=2).run(suite)
    timestr = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
    filename = timestr+'.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='result',
        description='report'
    )
    runner.run(suite)
    fp.close()