# -*- coding: utf-8 -*-
import time
from selenium import webdriver
import pandas as pd
import config
import os

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
    f1 = create_csvs()
    # click into Tags from side menu
    driver.find_element_by_class_name('open-tag-list-button').click()

    # create a dataframe with col names
    # put the tag names in first col
    # go one by one -> scrape tag name, click into it, scrape category, action, label

    for row in driver.find_elements_by_css_selector('tr.wd-tag-row'):
        tag_name = row.find_element_by_css_selector('a.open-tag-button')
        trigger = row.find_element_by_css_selector('a.small-trigger-chip')
        tag_type = row.find_element_by_xpath(".//td[3]")

        # print(tag_name.text)
        # print(trigger.text)
        print(tag_type.text)
        
        # Check if the current tag is a GA tag
        if tag_type.text == 'Google Analytics: Universal Analytics':
            print('yes')
            # if it is, then click into it and get category, action, label text
            # driver.find_element_by_css_selector('a.open-tag-button').click()
            # driver.find_element_by_css_selector('gtm-veditor-section-overlay').click()
        else:
            print('no')    
        

        # write values for each column to csv file
        # f1.write(tag_name.text + ',' + ' ,' + ' ,' + ' ,' + trigger.text + '\n')
    f1.close()
        
# create csv files
def create_csvs():
    if not os.path.exists('csv'):
        os.mkdir('csv')
    filename = f'csv/{config.account_to_audit}.csv'
    f1 = open(filename, 'w')
    headers = 'tag, trigger, category, action, label\n'
    f1.write(headers)
    return f1


site_login()
get_tags()
# driver.quit()