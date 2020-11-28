from selenium import webdriver
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
                self.login_button_1='//button[@class="css-1at8pli"][contains(text(),"LOGIN")]'
                self.login_button_2 = '//button[@class="css-e62wgj"][contains(text(),"Login")]'
                self.header_title = '//div[@id="root"]//header//h2//a[text()="Semicolon;"]'
                self.header_links = '//div[@id="root"]//header//a[contains(@href,"LINK")]'
                self.header_div = '//div[@id="root"]//header//parent::div'
                self.body_div = '//div[@id="root"]//div[contains(@class,"banner")]'
        def is_tag_element_visible(self, label,tag):
                driver.implicitly_wait(2000)
                text_element = driver.find_element_by_xpath(self.text_element.replace("LABEL", label).replace('TAG',tag))
                if text_element.is_displayed():
                        return True
                return False

        def verify_login_buttons(self):
                driver.implicitly_wait(2000)
                button1 = driver.find_element_by_xpath(self.login_button_1)
                button2 = driver.find_element_by_xpath(self.login_button_2)
                if button1.is_displayed() and button2 .is_displayed():
                        return  True
                return  False

        def verify_header_nonuser(self):
                driver.implicitly_wait(2000)
                header_elements = []
                header_elements.append(driver.find_element_by_xpath(self.header_title))
                header_elements.append(driver.find_element_by_xpath(self.header_links.replace("LINK","blogs")))
                header_elements.append(driver.find_element_by_xpath(self.header_links.replace("LINK", "register")))
                header_elements.append(driver.find_element_by_xpath(self.header_links.replace("LINK", "login")))
                for element in header_elements:
                        if not element.is_displayed():
                                return False
                return  True

        def verify_body_and_header_class(self,body_class,title_class):
                driver.implicitly_wait(2000)
                header = driver.find_element_by_xpath(self.header_div)
                body = driver.find_element_by_xpath(self.body_div)
                title_class_get = header.get_attribute('class')
                body_class_get = body.get_attribute('class')
                if title_class_get==title_class and body_class_get==body_class:
                        return True
                return False


