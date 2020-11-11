# -*- coding: utf-8 -*-
import time
from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome('/Users/Shared/chromedriver')

username = ''
password = ''
url = ''
account_to_audit = ''


def site_login():
    driver.get(url)
    driver.implicitly_wait(10) # this sets the default wait time for the rest of the WebDriver obect's life

    driver.find_element_by_id('identifierId').send_keys(username)
    driver.find_element_by_id('identifierNext').click()
    driver.find_element_by_class_name('vxx8jf').click()
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_id('passwordNext').click()

def get_account():
    # click into the account you want to audit
    driver.find_element_by_link_text(account_to_audit).click()

def get_tags():
    get_account()     
    # click into Tags from side menu
    driver.find_element_by_class_name('open-tag-list-button').click()


site_login()
get_tags()
# driver.quit()