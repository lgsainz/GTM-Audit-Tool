# -*- coding: utf-8 -*-
import time
from selenium import webdriver
import pandas as pd
import config

driver = webdriver.Chrome('/Users/Shared/chromedriver')

def site_login():
    driver.get(config.url)
    driver.implicitly_wait(10) # sets the default wait time for the rest of the WebDriver obect's life

    driver.find_element_by_id('identifierId').send_keys(config.username)
    driver.find_element_by_id('identifierNext').click()
    driver.find_element_by_class_name('vxx8jf').click()
    driver.find_element_by_name('password').send_keys(config.password)
    driver.find_element_by_id('passwordNext').click()

def get_account():
    # click into the account you want to audit
    driver.find_element_by_link_text(config.account_to_audit).click()

def get_tags():
    get_account()     
    # click into Tags from side menu
    driver.find_element_by_class_name('open-tag-list-button').click()

    # find tag names within table data
    # print(driver.find_elements_by_css_selector('a.open-tag-button')[0].text)
    for row in driver.find_elements_by_css_selector('a.open-tag-button'):
        print(row.text)


site_login()
get_tags()
# driver.quit()