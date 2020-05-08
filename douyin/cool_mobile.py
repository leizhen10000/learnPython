#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@file    :  cool_mobile.py
@time    :  20/3/4 20:41
@author  :  leizhen
@contact :  leizhen8080@foxmail.com
@desc    :
"""

from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.0'
desired_caps['deviceName'] = 'KVXBB18108203945'
desired_caps['appPackage'] = 'com.ss.android.ugc.aweme'
desired_caps['appActivity'] = '.main.MainActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
