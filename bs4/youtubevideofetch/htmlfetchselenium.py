import time
from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import urllib3

class Fetcher():

    def __init__(self, file, url):
        self.file = file
        self.url = url

    def updateFile(self):
        driver = webdriver.Chrome(executable_path='/Users/elizabethyoungblood/Documents/chromedriver')
        driver.get(self.url)

        time.sleep(2)

        try:
            signInButton = driver.find_element_by_class_name('signin-container')
            signInButton.click()
        except selenium.exceptions.NoSuchWindowException:
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

        with open(self.file, 'w', encoding='utf-8') as f:
            f.write(html_soup.prettify())
        driver.quit()
