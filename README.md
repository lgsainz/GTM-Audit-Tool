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
* Google Chrome

## Installing

How to get a development env running

### Install Selenium and additional python libraries

With:
```
pip install -r requirements.txt
```

### Chromedriver 

Check what version of Chrome you currently have. Download the corresponding webdriver (https://chromedriver.chromium.org/downloads/version-selection).

Once you've installed chromedriver, move it to /Users/Shared/chromedriver. This isn't mandatory - if you want to place it elsewhere, make sure to modify Line 7 in the code, to fit your current path.


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
