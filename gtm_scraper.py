from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import config
import os

driver = webdriver.Chrome('/Users/Shared/chromedriver')

# Google Tag Manager user/pass login
def site_login():
    driver.get(config.url)
    driver.implicitly_wait(5) # sets the default wait time for the rest of the WebDriver obect's life
    driver.find_element_by_id('identifierId').send_keys(config.username)
    driver.find_element_by_id('identifierNext').click()
   
    # check if current login screen is workspace selection or password field
    if len(driver.find_elements_by_class_name('vxx8jf')) > 0:
        driver.find_element_by_class_name('vxx8jf').click() # select workspace button

    driver.find_element_by_name('password').send_keys(config.password)
    driver.find_element_by_id('passwordNext').click()

# Select account to audit
def get_account():
    site_login()
    # click into the account you want to audit
    (WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, config.account_to_audit)))).click()

# Get all tags from container
def get_tags():
    get_account()
    f1 = create_csvs()

    # click into Tags from side menu
    driver.find_element_by_class_name('open-tag-list-button').click()

    # (do-while) to get tags
    write_tags(f1)
    # continue if pagination button is present
    while len(driver.find_elements_by_xpath("//i[@class='gtm-arrow-right-icon icon-button']")) > 0:
        (driver.find_element_by_xpath("//i[@class='gtm-arrow-right-icon icon-button']")).click()
        # print('next page!')
        write_tags(f1)
        
    f1.close()
    driver.quit()

def write_tags(filename):
     # get row within table
    for row in WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'tr.wd-tag-row'))):
        # wait for element located to contain text
        WebDriverWait(row, 10).until(lambda driver: row.find_element_by_css_selector('a.open-tag-button').text.strip() != '')
        tag_name = row.find_element_by_css_selector('a.open-tag-button')
        trigger = row.find_element_by_css_selector('a.small-trigger-chip')
        tag_type = row.find_element_by_xpath(".//td[3]")
        category, action, label = '', '', ''

        # Check if the current tag is a GA tag
        if tag_type.text == 'Google Analytics: Universal Analytics':
            # if so, click into tag and get category, action, label text
            tag_name.click()
            # click into overlay
            (WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'gtm-veditor-section-overlay')))).click()

            # get category, action, label (input text fields 1,2,3)
            category = (driver.find_element_by_xpath(".//gtm-vendor-template-text[1]//input")).get_attribute('value')
            action = (driver.find_element_by_xpath(".//gtm-vendor-template-text[2]//input")).get_attribute('value')
            label = (driver.find_element_by_xpath(".//gtm-vendor-template-text[3]//input")).get_attribute('value')

            driver.find_element_by_class_name('gtm-sheet-header__close').click() # click back to tags view
        
        # write values for each column to csv file
        filename.write(tag_name.text + ',' + category + ',' + action + ',' + label + ',' + trigger.text + '\n')
        
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
if __name__ == "__main__":
    get_tags()
