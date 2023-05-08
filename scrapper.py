"""

This file contains code that scraps web data of the specified url
and returns a json file based on the instructions.
The json file is used in the job_intents file to train the 
model for NLP search and chatbot creation.

Author: Austin (Github: sphinx-austin)

"""

import time
from selenium import webdriver
import requests
from bs4 import BeautifulSoup


# specific url website

# TEST
url = 'https://subslikescript.com/movies'

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
ul_scripts_list = soup.find('ul', class_='scripts-list')

for a in ul_scripts_list.find_all('a'):
    print(a.text)


# Using Selenium and Chromedriver

# create a chromedriver
driver = webdriver.Chrome('/Users/user/Downloads/chromedriver')

# navigate to the page
driver.get('https://')

# Wait 5 secs
time.sleep(5)

# find all elements with the specified xpath
elements = driver.find_elements_by_xpath("//span[@class='']")

# print the text attribute of the elements
for element in elements:
    print(element.text)


# clsoe browser
driver.quit()
