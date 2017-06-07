import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import urllib3

class Fetcher():

    def __init__(self):
        assert 1+1 == 2

    def updateFile(self, file, url):
        driver = webdriver.Chrome(executable_path='/Users/elizabethyoungblood/Documents/chromedriver')
        driver.get(url)

        time.sleep(2)

        try:
            signInButton = driver.find_element_by_class_name('signin-container')
            signInButton.click()
        except selenium.common.exceptions.NoSuchWindowException:
            signInButton = driver.find_element_by_id('ytd-formatted-string')
            signInButton.click()

        time.sleep(1.756)

        email = driver.find_element_by_name('identifier')
        email.send_keys('arghalexander3000@gmail.com')

        time.sleep(1)
        
        emailNext = driver.find_element_by_id('identifierNext')
        emailNext.click()

        time.sleep(1.5)

        password = driver.find_element_by_class_name('whsOnd')
        password.send_keys('D@vid875')

        time.sleep(1)

        passwordNext = driver.find_element_by_id('passwordNext')
        passwordNext.click()

        time.sleep(5)

        html_source = driver.page_source

        html_soup = BeautifulSoup(html_source, 'html.parser')

        with open(file, 'w', encoding='utf-8') as f:
            f.write(html_soup.prettify())
