import os

from crawlflow.request.abstractrequest import abstractRequest

from selenium import webdriver
from selenium.webdriver.common.by import By


class dinamicRequest(abstractRequest):
    def __init__(self, url):
        self.driver = webdriver.Chrome()
        self.url = url
    
    def open_driver(self):
        return self.driver.get("about:blank")

    def fetch_page(self):
        self.driver.get(self.url)
        
    def get_title(self):
        return self.driver.find_element(By.TAG_NAME, 'title').text
    
    def get_description(self):
        return self.driver.find_element(By.TAG_NAME, 'meta[name="description"]').get_attribute('content')
    
    def get_author(self):
        return self.driver.find_element(By.TAG_NAME, 'meta[name="author"]').get_attribute('content')
    
    def get_content(self):
        return self.driver.find_element(By.TAG_NAME, 'body').text
    
    def get_links(self):
        return self.driver.find_elements(By.TAG_NAME, 'a[href]')
    
    def get_metadata(self):
        return self.driver.find_elements(By.TAG_NAME, 'meta')
    
    def close(self):
        self.driver.close()