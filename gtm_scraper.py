# -*- coding: utf-8 -*-
import time
from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome('/Users/Shared/chromedriver')

username = ''
password = ''
url = ''

def site_login():
    driver.get(url)
    driver.find_element_by_id('identifierId').send_keys(username)
    driver.find_element_by_id('identifierNext').click()
    time.sleep(1)
    driver.find_element_by_class_name('vxx8jf').click()
    time.sleep(1)
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_id('passwordNext').click()
    time.sleep(3)

def get_tags():
    for table in driver.find_elements_by_xpath('//*[contains(@id,"ID")]//tr'):
        data = [item.text for item in table.find_elements_by_xpath(".//*[self::td or self::th]")]
        print(data)
    # time.sleep(3)

# site_login()
# get_tags()
driver.quit()