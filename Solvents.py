from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import os
import  time
import re
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(os.curdir + '/chromedriver',chrome_options=options)


def wait(sec=2):
        time.sleep(sec)
class Semicolon():
        def __init__(self):
                self.__url__ = "http://semicolon-blog.netlify.app/"
        def quit(self):
                driver.quit()
        def launchsemicolon(self):
                driver.get(self.__url__)
                wait()
        def launch_blogs_page(self):
                driver.get("https://semicolon-blog.netlify.app/blogs")
                wait()


class Solvents(Semicolon):
        def __init__(self):
                self.text_element = '//TAG[contains(text(),"LABEL")]'
                self.login_button_1='//button[@class="css-1at8pli"][contains(text(),"LOGIN")]'
                self.login_button_2 = '//button[@class="css-e62wgj"][contains(text(),"Login")]'
                self.header_title = '//div[@id="root"]//header//h2//a[text()="Semicolon;"]'
                self.header_links = '//div[@id="root"]//header//a[contains(@href,"LINK")]'
                self.header_div = '//div[@id="root"]//header//parent::div'
                self.body_div = '//div[@id="root"]//div[contains(@class,"banner")]'
                self.email_input = '//input[@id="email"]'
                self.password_input = '//input[@id="password"]'
                self.login_message = '//div[contains(text(),"Logged in !")]'
                self.blog_page_title = '//h2[contains(text(),"Trending Blogs")]'
                self.blog_heading_class = '//h2[@class="css-1g49eu2"]'
                self.blog_title = self.blog_heading_class+'[contains(text(),"NAME")]'
                self.blog_link = '//a[contains(@href,"NAME")]'
                self.blog_img = self.blog_link+'//descendant::img[contains(@class,"blog-banner")]'
                self.blog_div = '//div[@id="container"]'
                self.blog_name = self.blog_div+'//h2[contains(text(),"NAME")]'
                self.blog_banner_img = self.blog_div+'//img[contains(@class,"css-muypb7")]'
                self.new_blog_button = '//button//a[contains(@href,"new")]//p[contains(text(),"NEW BLOG")]'
        def is_tag_element_visible(self, label,tag):
                text_element = driver.find_element_by_xpath(self.text_element.replace("LABEL", label).replace('TAG',tag))
                if text_element.is_displayed():
                        return True
                return False
        def verify_login_buttons(self):
                button1 = driver.find_element_by_xpath(self.login_button_1)
                button2 = driver.find_element_by_xpath(self.login_button_2)
                if button1.is_displayed() and button2 .is_displayed():
                        return  True
                return  False
        def verify_header_nonuser(self):
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
                header = driver.find_element_by_xpath(self.header_div)
                body = driver.find_element_by_xpath(self.body_div)
                title_class_get = header.get_attribute('class')
                body_class_get = body.get_attribute('class')
                if title_class_get==title_class and body_class_get==body_class:
                        return True
                return False
        def click_header_explore_link(self):
                header_explore_link = driver.find_element_by_xpath(self.header_links.replace("LINK","blogs"))
                header_explore_link.click()
        def get_current_url(self):
                wait()
                return driver.current_url
        def click_button(self,label):
                wait()
                button = driver.find_element_by_xpath(self.text_element.replace("TAG","button").replace("LABEL",label))
                button.click()
        def click_header_login_button(self):
                wait()
                login = driver.find_element_by_xpath(self.login_button_1)
                login.click()
        def add_login_details(self,email,pwd):
                email_input = driver.find_element_by_xpath(self.email_input)
                pwd_input = driver.find_element_by_xpath(self.password_input)
                email_input.send_keys(email)
                wait()
                pwd_input.send_keys(pwd)
                wait()
        def click_submit_login_button(self):
                wait()
                login = driver.find_element_by_xpath(self.login_button_2.replace("css-e62wgj","css-1mvezxw"))
                login.click()
        def click_link(self,label):
                wait()
                link = driver.find_element_by_xpath(self.text_element.replace("TAG","a").replace("LABEL",label))
                link.click()
        def switch_to_last_tab(self):
                driver.switch_to.window(driver.window_handles[-1])
        def switch_to_first_tab(self):
                driver.switch_to.window(driver.window_handles[0])
        def is_login_msg_displayed(self):
                msg = driver.find_element_by_xpath(self.login_message)
                return msg.is_displayed()
        def is_blog_page_title_displayed(self):
                title = driver.find_element_by_xpath(self.blog_page_title)
                return title.is_displayed()
        def scroll_till_label(self,label):
                ele = driver.find_element_by_xpath(self.text_element.replace("TAG","*").replace("LABEL",label))
                actions = ActionChains(driver)
                actions.move_to_element(ele).perform()
        def is_blog_title_displayed(self,label):
                title = driver.find_element_by_xpath(self.blog_title.replace("NAME",label))
                wait()
                self.scroll_till_label(label)
                wait()
                return title.is_displayed()
        def label_to_link_label(self,label):
                link_label = label.lower()
                link_label = re.sub(r'[^\w\s]', '', link_label)
                link_label = link_label.strip()
                link_label = " ".join(link_label.split())
                link_label = link_label.replace(" ", "-")
                return  link_label
        def is_blog_link_displayed(self, label):
                link_label = self.label_to_link_label(label)
                link = driver.find_element_by_xpath(self.blog_link.replace("NAME", link_label))
                wait()
                self.scroll_till_label(label)
                wait()
                return link.is_displayed()
        def is_blog_image_displayed(self, label):
                link_label = self.label_to_link_label(label)
                img = driver.find_element_by_xpath(self.blog_img.replace("NAME", link_label))
                wait()
                self.scroll_till_label(label)
                wait()
                return img.is_displayed()
        def click_blog_title_by_name(self,label):
                title = driver.find_element_by_xpath(self.blog_title.replace("NAME", label))
                wait()
                self.scroll_till_label(label)
                wait()
                title.click()
        def is_blog_view_title_displayed(self,name):
                title = driver.find_element_by_xpath(self.blog_name.replace("NAME",name))
                return  title.is_displayed()
        def is_blog_view_image_displayed(self):
                img = driver.find_element_by_xpath(self.blog_banner_img)
                return  img.is_displayed()
        def is_link_displayed(self,url):
                link = driver.find_element_by_xpath(self.blog_link.replace("NAME",url))
                return link.is_displayed()
        def is_new_blog_button_displayed(self):
                button = driver.find_element_by_xpath(self.new_blog_button)
                return button.is_displayed()
        def click_new_blog_button(self):
                button = driver.find_element_by_xpath(self.new_blog_button)
                button.click()
