from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os
import  time
import re
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

def wait(sec=5):
        time.sleep(sec)
class Semicolon():
        def __init__(self):
                self.__url__ = "http://localhost:3000/"
        def quit(self):
                global driver
                driver.quit()
        def create_driver(self):
                global  driver
                driver = webdriver.Chrome(os.curdir + '/chromedriver',chrome_options=options)
        def launchsemicolon(self):
                global driver
                driver.get(self.__url__)
                wait()
        def launch_blogs_page(self):
                global driver
                driver.get(self.__url__+"blogs")
                wait()

class Solvents(Semicolon):
        email_user1 = 'user1@semicolon.com'
        pwd_user1 = 'semicolon/test'
        def __init__(self):
                self.tag_element = '//TAG[contains(text(),"LABEL")]'
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
                self.blog_view_div = '//div[@id="container"]'
                self.blog_view_title = self.blog_view_div + '//h2[contains(text(),"NAME")]'
                self.blog_view_banner_img = self.blog_view_div + '//img[contains(@class,"css-muypb7")]'
                self.new_blog_button = '//button//a[contains(@href,"new")]//p[contains(text(),"NEW BLOG")]'
                self.unregistered_user_alert = '//div[@role="alert"]//div[contains(text(),"Invalid Credentials. Please check again.")]'
                self.new_blog_page = '//form'
                self.new_blog_page_title = self.new_blog_page+'//h2[contains(text(),"New Blog")]'
                self.new_blog_input_textarea = self.new_blog_page+'//textarea[contains(@class,"editor")]'
                self.new_blog_input_markdown_preview = self.new_blog_page + '//div[contains(@class,"markdown")]'
                self.new_blog_image_url_input = self.new_blog_page+'//input[contains(@name,"bannerURL")][@type="url"]'
                self.new_blog_name_input = self.new_blog_page + '//input[contains(@name,"title")][@type="text"]'
                self.new_blog_toolbar = self.new_blog_page+'//div[contains(@class,"editor-toolbar")]'

        def generate_toolbar_dict(self):
                toolbar_buttons = {}
                toolbar_buttons["bold"]=self.new_blog_toolbar+'//button[contains(@data-name,"bold")]'
                toolbar_buttons["italic"]= self.italic_button = self.new_blog_toolbar + '//button[contains(@data-name,"italic")]'
                toolbar_buttons["strikethrough"]=self.strikethrough_button = self.new_blog_toolbar + '//button[contains(@data-name,"strikethrough")]'
                toolbar_buttons["hr"]=self.hr_button = self.new_blog_toolbar + '//button[@data-name = "hr"]'
                toolbar_buttons["title"]=self.title_button = self.new_blog_toolbar + '//button[contains(@data-name,"title")]'
                toolbar_buttons["link"]=self.link_button = self.new_blog_toolbar + '//button[contains(@data-name,"link")]'
                toolbar_buttons["quote"]=self.quote_button = self.new_blog_toolbar + '//button[contains(@data-name,"quote")]'
                toolbar_buttons["code"]=self.code_button = self.new_blog_toolbar + '//button[contains(@data-name,"code")]'
                toolbar_buttons["image"]=self.image_button = self.new_blog_toolbar + '//button[contains(@data-name,"image")]'
                toolbar_buttons["unordered-list"]=self.unordered_button = self.new_blog_toolbar + '//button[@data-name="unordered-list"]'
                toolbar_buttons["ordered-list"]=self.ordered_button = self.new_blog_toolbar + '//button[@data-name="ordered-list"]'
                toolbar_buttons["checked-list"]=self.checked_button = self.new_blog_toolbar + '//button[contains(@data-name,"checked-list")]'
                toolbar_buttons["edit"]=self.edit_button = self.new_blog_toolbar + '//button[contains(@data-name,"edit")]'
                toolbar_buttons["live"]=self.live_button = self.new_blog_toolbar + '//button[contains(@data-name,"live")]'
                toolbar_buttons["preview"]=self.preview_button = self.new_blog_toolbar + '//button[contains(@data-name,"preview")]'
                toolbar_buttons["fullscreen"]=self.fullscreen_button = self.new_blog_toolbar + '//button[contains(@data-name,"fullscreen")]'
                return  toolbar_buttons
        def generate_markdown_dict(self):
                tags = {}
                tags["bold"]= self.new_blog_input_markdown_preview+'//strong'
                tags["italic"]=self.new_blog_input_markdown_preview+'//em'
                tags["strikethrough"]=self.new_blog_input_markdown_preview+'//del'
                tags["hr"]=self.new_blog_input_markdown_preview+'//hr'
                tags["title"]=self.new_blog_input_markdown_preview+'//h2'
                tags["link"]=self.new_blog_input_markdown_preview+'//a'
                tags["quote"]=self.new_blog_input_markdown_preview+'//blockquote'
                tags["code"]=self.new_blog_input_markdown_preview+'//code'
                tags["image"]=self.new_blog_input_markdown_preview+'//img'
                tags["unordered-list"]=self.new_blog_input_markdown_preview+'//ul'
                tags["ordered-list"]=self.new_blog_input_markdown_preview+'//ol'
                tags["checked-list"]=self.new_blog_input_markdown_preview+'//ul'
                tags["unordered-list-element"] = self.new_blog_input_markdown_preview + '//ul//li'
                tags["ordered-list-element"]=self.new_blog_input_markdown_preview+'//ol//li'
                tags["checked-list-element"] = self.new_blog_input_markdown_preview + '//ul//li'
                return  tags
        def is_tag_element_visible(self, label,tag):
                element = driver.find_element_by_xpath(self.tag_element.replace("LABEL", label).replace('TAG', tag))
                try: return element.is_displayed()
                except: return False
        def is_tag_element_disabled(self,label,tag):
                ele = driver.find_element_by_xpath(self.tag_element.replace("LABEL", label).replace('TAG', tag))
                try: return ele.get_attribute("aria-disabled")=="true"
                except: return  False
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
                button = driver.find_element_by_xpath(self.tag_element.replace("TAG", "button").replace("LABEL", label))
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
                link = driver.find_element_by_xpath(self.tag_element.replace("TAG", "a").replace("LABEL", label))
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
                ele = driver.find_element_by_xpath(self.tag_element.replace("TAG", "*").replace("LABEL", label))
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
                title = driver.find_element_by_xpath(self.blog_view_title.replace("NAME", name))
                return  title.is_displayed()
        def is_blog_view_image_displayed(self):
                img = driver.find_element_by_xpath(self.blog_view_banner_img)
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
        def click_log_out_button(self):
                button = driver.find_element_by_xpath(self.tag_element.replace("TAG", "button").replace("LABEL", "LOG OUT"))
                button.click()
        def is_user_logged_in(self):
                try:
                        return self.is_new_blog_button_displayed()
                except:
                        return False
        def login(self,email,pwd):
                self.add_login_details(email, pwd)
                wait()
                self.click_submit_login_button()
                wait(4)
                try:
                        return self.is_login_msg_displayed()
                except:return False
        def is_log_out_msg_displayed(self):
                msg = driver.find_element_by_xpath(self.tag_element.replace("LABEL","Successfully logged out.").replace("TAG","div"))
                try: return msg.is_displayed()
                except: return False
        def is_unregistered_user_alert_visible(self):
                alert = driver.find_element_by_xpath(self.unregistered_user_alert)
                return alert.is_displayed()
        def is_new_blog_page_title(self):
                title = driver.find_element_by_xpath(self.new_blog_page_title)
                return title.is_displayed()
        def is_new_blog_title_input_visible(self):
                ele = driver.find_element_by_xpath(self.new_blog_name_input)
                return ele.is_displayed()
        def is_new_blog_image_input_visible(self):
                ele = driver.find_element_by_xpath(self.new_blog_image_url_input)
                return ele.is_displayed()
        def is_new_blog_textarea_input_visible(self):
                ele = driver.find_element_by_xpath(self.new_blog_input_textarea)
                return ele.is_displayed()
        def is_new_blog_markdown_preview_visible(self):
                ele = driver.find_element_by_xpath(self.new_blog_input_markdown_preview)
                return ele.is_displayed()
        def verify_toolbar_buttons(self,button):
                toolbar_buttons = self.generate_toolbar_dict()
                button = driver.find_element_by_xpath(toolbar_buttons[button])
                try: return button.is_displayed()
                except: return  False
        def click_toolbar_button(self,button):
                toolbar_buttons = self.generate_toolbar_dict()
                button = driver.find_element_by_xpath(toolbar_buttons[button])
                button.click()
        def go_to_new_blog_page(self):
                ret = False
                if not self.is_user_logged_in():
                        self.click_header_login_button()
                        if 'user/login' in self.get_current_url(): ret = True
                        else: ret = False
                        if self.login(self.email_user1, self.pwd_user1): ret = True
                        else: ret = False
                if self.is_new_blog_button_displayed(): ret = True
                else: ret=False
                self.click_new_blog_button()
                return  ret
        def send_keys_to_editor(self,text):
                textarea = driver.find_element_by_xpath(self.new_blog_input_textarea)
                textarea.send_keys(text)
                wait(2)
        def clear_text_area(self):
                textarea = driver.find_element_by_xpath(self.new_blog_input_textarea)
                textarea.clear()
                wait(2)
        def get_text_area_contents(self):
                textarea = driver.find_element_by_xpath(self.new_blog_input_textarea)
                return textarea.text
        def get_markdown_preview_contents(self,tag=""):
                if tag == "": ele = driver.find_element_by_xpath(self.new_blog_input_markdown_preview+'//p')
                else:
                        mark_down_dict = self.generate_markdown_dict()
                        ele = driver.find_element_by_xpath(mark_down_dict[tag])
                        if tag == 'hr' or tag == "image": return  ele.is_displayed()
                return  ele.text
        def undo(self):
                action = ActionChains(driver)
                action.key_down(Keys.CONTROL).send_keys('z').key_up(Keys.CONTROL).perform()
                wait(2)
        def select_all(self):
                action = ActionChains(driver)
                action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
                wait(2)
        def enter(self):
                action = ActionChains(driver)
                action.key_down(Keys.ENTER).perform()
                wait(2)
        def set_link_in_textarea(self,text,url):
                wait(1)
                self.click_toolbar_button("link")
                self.send_keys_to_editor(text)
                wait(1)
                get = self.get_text_area_contents()
                self.clear_text_area()
                self.send_keys_to_editor(get.replace("url",url))
        def verify_link_preview_markdown(self,url):
                mark_down_dict = self.generate_markdown_dict()
                ele = driver.find_element_by_xpath(mark_down_dict["link"])
                try: ele.is_displayed()
                except:
                        return False
                if url in ele.get_attribute("href"): return  True
        def set_image_in_textarea(self,text,url):
                wait(1)
                self.click_toolbar_button("image")
                self.send_keys_to_editor(url)
                wait(1)
                get = self.get_text_area_contents()
                self.clear_text_area()
                self.send_keys_to_editor(get[:2]+text+get[2:])
        def verify_image_preview_markdown(self, text,url):
                mark_down_dict = self.generate_markdown_dict()
                ele = driver.find_element_by_xpath(mark_down_dict["image"])
                try:
                        ele.is_displayed()
                except:
                        return False
                if url in ele.get_attribute("src") and text in ele.get_attribute("alt"): return True
        def set_list_in_textarea(self,type,values):
                wait(1)
                for text in values:
                        self.send_keys_to_editor(text)
                        self.enter()
                self.select_all()
                self.click_toolbar_button(type)
                wait(1)
        def verify_list_preview_markdown(self,type,values):
                mark_down_dict = self.generate_markdown_dict()
                for i in range(len(values)):
                        ele = driver.find_element_by_xpath(mark_down_dict[type+"-element"]+"["+str(i+1)+"]")
                        if type == "checked-list":
                                ele1 = driver.find_element_by_xpath(
                                        mark_down_dict[type + "-element"] + "[" + str(i + 1) + "]//input")
                                try:
                                        if ele1.is_displayed(): pass
                                except: return False
                        if ele.text not in values : return  False
                return  True

