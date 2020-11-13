# -*- coding: utf-8 -*-
import time
from selenium import webdriver
import config
import os

driver = webdriver.Chrome('/Users/Shared/chromedriver')

def site_login():
    driver.get(config.url)
    driver.implicitly_wait(10) # sets the default wait time for the rest of the WebDriver obect's life

    driver.find_element_by_id('identifierId').send_keys(config.username)
    driver.find_element_by_id('identifierNext').click()
    driver.find_element_by_class_name('vxx8jf').click() # select workspace button (check: is this always a step?)
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

    for row in driver.find_elements_by_css_selector('tr.wd-tag-row'):
        tag_name = row.find_element_by_css_selector('a.open-tag-button')
        trigger = row.find_element_by_css_selector('a.small-trigger-chip')
        tag_type = row.find_element_by_xpath(".//td[3]")
        category, action, label = '', '', ''

        # Check if the current tag is a GA tag
        if tag_type.text == 'Google Analytics: Universal Analytics':
            # if so, click into tag and get category, action, label text
            tag_name.click()
            driver.find_element_by_class_name('gtm-veditor-section-overlay').click() # click into overlay

            # get category, action, label (input text fields 1,2,3)
            category = (driver.find_element_by_xpath(".//gtm-vendor-template-text[1]//input")).get_attribute('value')
            action = (driver.find_element_by_xpath(".//gtm-vendor-template-text[2]//input")).get_attribute('value')
            label = (driver.find_element_by_xpath(".//gtm-vendor-template-text[3]//input")).get_attribute('value')

            driver.find_element_by_class_name('gtm-sheet-header__close').click() # click back to tags view
        
        # write values for each column to csv file
        f1.write(tag_name.text + ',' + category + ',' + action + ',' + label + ',' + trigger.text + '\n')
        time.sleep(0.5) # to prevent skipping tags

    f1.close()
        
# create csv files
def create_csvs():
    if not os.path.exists('csv'):
        os.mkdir('csv')
    filename = f'csv/{config.account_to_audit}.csv'
    f1 = open(filename, 'w')
    headers = 'tag, category, action, label, trigger\n'
    f1.write(headers)
    return f1

# execute program
site_login()
get_tags()
driver.quit()