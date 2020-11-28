from selenium import webdriver
from selenium.webdriver.common.by import By
import os

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(os.curdir + '/chromedriver',chrome_options=options)


class Semicolon():

        def __init__(self):
                self.__url__ = "http://semicolon-blog.netlify.app/"

        def close_driver(self):
                driver.close()

        def launchsemicolon(self):
                driver.get(self.__url__)


class Solvents(Semicolon):
        def __init__(self):
                self.text_element = '//TAG[contains(text(),"LABEL")]'
                #self.button_std = '//button[contains(text(),"LABEL")]'

        def is_tag_element_visible(self, label,tag):
                driver.implicitly_wait(2000)
                text_element = driver.find_element_by_xpath(self.text_element.replace("LABEL", label).replace('TAG',tag))
                if text_element.is_displayed():
                        return True
                return False
