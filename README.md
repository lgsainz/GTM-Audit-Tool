# GTM Web Scrape Tool

This project was created only for educational proposes and to be used on a user's personal account.
Used Python and Selenium.
**Important: Educational Purposes Only**

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites

What you need:

* Python 3.x (and pip)
* Chromedriver
* Google Chrome (you can use another browser)

## Installing

A step by step series of examples that tell you how to get a development env running

### Install the following Python libraries:

 * **requests2** - Requests is the only Non-GMO HTTP library for Python, safe for human consumption;
 * **pandas** - A great Python Data Analysis Library;
 * **lxml** - Library for processing XML and HTML;
 * **beautfulsoup4** - Library for pulling data out of HTML and XML files;
 * **selenium** - An API to write functional/acceptance tests using Selenium WebDriver.

With:
```
pip install -r requirements.txt
```

### Chromedriver 

Check what version of Chrome you currently have. Download the corresponding webdriver (https://chromedriver.chromium.org/downloads/version-selection).


## Running the code

You will need to create a config.py file to include credentials and account information. The contents of this file should look as follows:

```python
username = ''
password = ''
url = ''
account_to_audit = ''
```

When your ready, run the program:

```
python gtm_scraper.py
```
