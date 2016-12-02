#!/usr/bin/python
#-*-coding:utf-8-*-
from appium import webdriver

class SetupConfig():
    def SetupAppium(test_os='Android',test_version='5.1.1',test_device='NHG6T16506000967',test_app='com.htmm.owner',test_Activity='.activity.main.SplashActivity'):
        desired_capabilities = {}
        desired_capabilities['platformName'] = test_os
        desired_capabilities['platformVersion'] = test_version
        desired_capabilities['deviceName'] = test_device
        desired_capabilities['appPackage'] = test_app
        desired_capabilities['appActivity'] = test_Activity
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities)
        return driver
        
    def SetupAppium1(test_os='Android',test_version='5.1.1',test_device='NHG6T16506000967',test_app='com.htmm.owner',test_Activity='.activity.main.MainActivity'):
        desired_capabilities = {}
        desired_capabilities['platformName'] = test_os
        desired_capabilities['platformVersion'] = test_version
        desired_capabilities['deviceName'] = test_device
        desired_capabilities['appPackage'] = test_app
        desired_capabilities['appActivity'] = test_Activity
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities)
        return driver
        
    #def NetworkStatus(driver):
    
    
