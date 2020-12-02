from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os
import time
import re
import pymongo

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")


def wait(sec=5):
        time.sleep(sec)


class Semicolon():
        def __init__(self):
                self.__url__ = "http://localhost:3000/"

        def quit(self):
                global driver
                print("Webdriver closed<br>")
                driver.quit()

        def create_driver(self):
                global driver
                print("Launch Webdriver- Chrome<br>")
                driver = webdriver.Chrome(os.curdir + '/chromedriver', chrome_options=options)

        def launchsemicolon(self):
                global driver
                driver.get(self.__url__)
                print("Launch URL: " + self.__url__ + "<br>")
                wait()

        def launch_blogs_page(self):
                global driver
                driver.get(self.__url__ + "blogs")
                print("Launch URL: " + self.__url__ + "blog <br>")
                wait()

        def delete_blog(self, name):
                myclient = pymongo.MongoClient("mongodb://localhost:27017/")
                mydb = myclient["blogdb"]
                mycol = mydb["blogs"]
                myquery = {"title": name}
                print("Delete Blog with Title: " + name + "<br>")
                mycol.delete_one(myquery)

        def delete_user(self, name):
                myclient = pymongo.MongoClient("mongodb://localhost:27017/")
                mydb = myclient["blogdb"]
                mycol = mydb["users"]
                myquery = {"username": name}
                print("Delete User with Username: " + name + "<br>")
                mycol.delete_one(myquery)


class Solvents(Semicolon):
        email_user1 = 'user1@semicolon.com'
        pwd_user1 = 'semicolon/test'

        def __init__(self):
                self.tag_element = '//TAG[contains(text(),"LABEL")]'
                self.login_button_1 = '//button[@class="css-1at8pli"][contains(text(),"LOGIN")]'
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
                self.blog_title = self.blog_heading_class + '[contains(text(),"NAME")]'
                self.blog_link = '//a[contains(@href,"NAME")]'
                self.blog_img = self.blog_link + '//descendant::img[contains(@class,"blog-banner")]'
                self.blog_view_div = '//div[@id="container"]'
                self.blog_view_title = self.blog_view_div + '//h2[contains(text(),"NAME")]'
                self.blog_view_banner_img = self.blog_view_div + '//img[contains(@class,"css-muypb7")]'
                self.new_blog_button = '//button//a[contains(@href,"new")]//p[contains(text(),"NEW BLOG")]'
                self.unregistered_user_alert = '//div[@role="alert"]//div[contains(text(),"Invalid Credentials. Please check again.")]'
                self.new_blog_page = '//form'
                self.new_blog_page_title = self.new_blog_page + '//h2[contains(text(),"New Blog")]'
                self.new_blog_input_textarea = self.new_blog_page + '//textarea[contains(@class,"editor")]'
                self.new_blog_input_markdown_preview = self.new_blog_page + '//div[contains(@class,"markdown")]'
                self.new_blog_image_url_input = self.new_blog_page + '//input[contains(@name,"bannerURL")][@type="url"]'
                self.new_blog_name_input = self.new_blog_page + '//input[contains(@name,"title")][@type="text"]'
                self.new_blog_toolbar = self.new_blog_page + '//div[contains(@class,"editor-toolbar")]'
                self.new_blog_fullscreen = self.new_blog_page + '//div[contains(@class,"w-md-editor-content")][contains(@style,"100%")]'
                self.uname_input = '//input[@id="username"]'
                self.admin_table_blog_title = '//table//tbody//tr//td[2]'
                self.admin_table_blog_author = '//table//tbody//tr//td[4]'
                self.admin_table_blog_status = '//table//tbody//tr//td[7]'
                self.approve_button = '//td[contains(text(),"Title")]//following-sibling::td//button[contains(text(),"Approve")]'

        def generate_toolbar_dict(self):
                toolbar_buttons = {}
                toolbar_buttons["bold"] = self.new_blog_toolbar + '//button[contains(@data-name,"bold")]'
                toolbar_buttons[
                        "italic"] = self.italic_button = self.new_blog_toolbar + '//button[contains(@data-name,"italic")]'
                toolbar_buttons[
                        "strikethrough"] = self.strikethrough_button = self.new_blog_toolbar + '//button[contains(@data-name,"strikethrough")]'
                toolbar_buttons["hr"] = self.hr_button = self.new_blog_toolbar + '//button[@data-name = "hr"]'
                toolbar_buttons[
                        "title"] = self.title_button = self.new_blog_toolbar + '//button[contains(@data-name,"title")]'
                toolbar_buttons[
                        "link"] = self.link_button = self.new_blog_toolbar + '//button[contains(@data-name,"link")]'
                toolbar_buttons[
                        "quote"] = self.quote_button = self.new_blog_toolbar + '//button[contains(@data-name,"quote")]'
                toolbar_buttons[
                        "code"] = self.code_button = self.new_blog_toolbar + '//button[contains(@data-name,"code")]'
                toolbar_buttons[
                        "image"] = self.image_button = self.new_blog_toolbar + '//button[contains(@data-name,"image")]'
                toolbar_buttons[
                        "unordered-list"] = self.unordered_button = self.new_blog_toolbar + '//button[@data-name="unordered-list"]'
                toolbar_buttons[
                        "ordered-list"] = self.ordered_button = self.new_blog_toolbar + '//button[@data-name="ordered-list"]'
                toolbar_buttons[
                        "checked-list"] = self.checked_button = self.new_blog_toolbar + '//button[contains(@data-name,"checked-list")]'
                toolbar_buttons[
                        "edit"] = self.edit_button = self.new_blog_toolbar + '//button[contains(@data-name,"edit")]'
                toolbar_buttons[
                        "live"] = self.live_button = self.new_blog_toolbar + '//button[contains(@data-name,"live")]'
                toolbar_buttons[
                        "preview"] = self.preview_button = self.new_blog_toolbar + '//button[contains(@data-name,"preview")]'
                toolbar_buttons[
                        "fullscreen"] = self.fullscreen_button = self.new_blog_toolbar + '//button[contains(@data-name,"fullscreen")]'
                print("Generate Toolbar Dictionary<br>")
                return toolbar_buttons

        def generate_markdown_dict(self):
                tags = {}
                tags["bold"] = self.new_blog_input_markdown_preview + '//strong'
                tags["italic"] = self.new_blog_input_markdown_preview + '//em'
                tags["strikethrough"] = self.new_blog_input_markdown_preview + '//del'
                tags["hr"] = self.new_blog_input_markdown_preview + '//hr'
                tags["title"] = self.new_blog_input_markdown_preview + '//h2'
                tags["link"] = self.new_blog_input_markdown_preview + '//a'
                tags["quote"] = self.new_blog_input_markdown_preview + '//blockquote'
                tags["code"] = self.new_blog_input_markdown_preview + '//code'
                tags["image"] = self.new_blog_input_markdown_preview + '//img'
                tags["unordered-list"] = self.new_blog_input_markdown_preview + '//ul'
                tags["ordered-list"] = self.new_blog_input_markdown_preview + '//ol'
                tags["checked-list"] = self.new_blog_input_markdown_preview + '//ul'
                tags["unordered-list-element"] = self.new_blog_input_markdown_preview + '//ul//li'
                tags["ordered-list-element"] = self.new_blog_input_markdown_preview + '//ol//li'
                tags["checked-list-element"] = self.new_blog_input_markdown_preview + '//ul//li'
                print("Generate Markdown Dictionary<br>")
                return tags

        def generate_blog_dict(self):
                tags = {}
                tags["bold"] = '//div[contains(@class,"md-content")]//strong'
                tags["italic"] = '//div[contains(@class,"md-content")]//em'
                tags["strikethrough"] = '//div[contains(@class,"md-content")]//del'
                tags["hr"] = '//div[contains(@class,"md-content")]//hr'
                tags["title"] = '//div[contains(@class,"md-content")]//h2//span'
                tags["link"] = '//div[contains(@class,"md-content")]//a'
                tags["quote"] = '//div[contains(@class,"md-content")]//code//span'
                tags["code"] = '//div[contains(@class,"md-content")]//h2//code'
                tags["image"] = '//div[contains(@class,"md-content")]//img'
                print("Generate Blog Content Dictionary<br>")
                return tags

        def is_tag_element_visible(self, label, tag):
                element = driver.find_element_by_xpath(self.tag_element.replace("LABEL", label).replace('TAG', tag))
                try:
                        if element.is_displayed():
                                print(tag + " with label: " + label + "  displayed<br>")
                                return True
                        else:
                                print(tag + " with label: " + label + " not displayed<br>")
                                return False
                except:
                        print(tag + " with label: " + label + " not displayed<br>")
                        return False

        def is_tag_element_disabled(self, label, tag):
                ele = driver.find_element_by_xpath(self.tag_element.replace("LABEL", label).replace('TAG', tag))
                try:
                        if ele.get_attribute("aria-disabled") == "true":
                                print(tag + " with label: " + label + "  displayed<br>")
                                return True
                        else:
                                print(tag + " with label: " + label + " not displayed<br>")
                                return False
                except:
                        print(tag + " with label: " + label + " not displayed<br>")
                        return False

        def verify_login_buttons(self):
                button1 = driver.find_element_by_xpath(self.login_button_1)
                button2 = driver.find_element_by_xpath(self.login_button_2)
                if button1.is_displayed() and button2.is_displayed():
                        print("Login Buttons Displayed<br>")
                        return True
                print("Login Buttons not displayed<br>")
                return False

        def verify_header_nonuser(self):
                header_elements = []
                header_elements.append(driver.find_element_by_xpath(self.header_title))
                header_elements.append(driver.find_element_by_xpath(self.header_links.replace("LINK", "blogs")))
                header_elements.append(driver.find_element_by_xpath(self.header_links.replace("LINK", "register")))
                header_elements.append(driver.find_element_by_xpath(self.header_links.replace("LINK", "login")))
                for element in header_elements:
                        if not element.is_displayed():
                                print("Header for Non-user not displayed<br>")
                                return False
                print("Header for Non-user displayed<br>")
                return True

        def verify_body_and_header_class(self, body_class, title_class):
                header = driver.find_element_by_xpath(self.header_div)
                body = driver.find_element_by_xpath(self.body_div)
                title_class_get = header.get_attribute('class')
                body_class_get = body.get_attribute('class')
                if title_class_get == title_class and body_class_get == body_class:
                        print("Body and Header class correct<br>")
                        return True
                print("Body and Header class incorrect<br>")
                return False

        def click_header_explore_link(self):
                header_explore_link = driver.find_element_by_xpath(self.header_links.replace("LINK", "blogs"))
                try:
                        header_explore_link.click()
                        print("Header explore link clicked<br>")
                except:
                        print("Header explore link clicked<br>")

        def get_current_url(self):
                wait()
                print("Current URL: " + driver.current_url + "<br>")
                return driver.current_url

        def click_button(self, label):
                wait()
                button = driver.find_element_by_xpath(self.tag_element.replace("TAG", "button").replace("LABEL", label))
                try:
                        button.click()
                        print(label + " button  clicked<br>")
                except:
                        print(label + " button  clicked<br>")

        def click_header_login_button(self):
                wait()
                login = driver.find_element_by_xpath(self.login_button_1)
                try:
                        login.click()
                        print("Login button clicked<br>")
                except:
                        print("Login button clicked<br>")

        def add_login_details(self, email, pwd):
                email_input = driver.find_element_by_xpath(self.email_input)
                pwd_input = driver.find_element_by_xpath(self.password_input)
                email_input.send_keys(email)
                wait()
                pwd_input.send_keys(pwd)
                print("Login details: <br>Email: " + email + "<br>Password" + pwd + "<br>")
                wait()

        def click_submit_login_button(self):
                wait()
                login = driver.find_element_by_xpath(self.login_button_2.replace("css-e62wgj", "css-1mvezxw"))
                try:
                        login.click()
                        print("Submit Login button  clicked<br>")
                except:
                        print("Submit Login button clicked<br>")

        def click_link(self, label):
                wait()
                link = driver.find_element_by_xpath(self.tag_element.replace("TAG", "a").replace("LABEL", label))
                try:
                        link.click()
                        print(label + " link clicked<br>")
                except:
                        print(label + " link clicked<br>")

        def switch_to_last_tab(self):
                driver.switch_to.window(driver.window_handles[-1])
                print("Switched to last tab<br>")

        def switch_to_first_tab(self):
                driver.switch_to.window(driver.window_handles[0])
                print("Switched to first tab<br>")

        def is_login_msg_displayed(self):
                msg = driver.find_element_by_xpath(self.login_message)
                if msg.is_displayed():
                        print("Login message displayed<br>")
                        return True
                else:
                        print("Login message not displayed<br>")
                        return False

        def is_blog_page_title_displayed(self):
                title = driver.find_element_by_xpath(self.blog_page_title)
                if title.is_displayed():
                        print("Blog page title displayed<br>")
                        return True
                else:
                        print("Blog page title not displayed<br>")
                        return False

        def scroll_till_label(self, label):
                ele = driver.find_element_by_xpath(self.tag_element.replace("TAG", "*").replace("LABEL", label))
                actions = ActionChains(driver)
                actions.move_to_element(ele).perform()
                print("Scrolling to element with label: " + label + "<br>")

        def is_blog_title_displayed(self, label):
                title = driver.find_element_by_xpath(self.blog_title.replace("NAME", label))
                wait()
                self.scroll_till_label(label)
                wait()
                return title.is_displayed()
                if title.is_displayed():
                        print("Blog title displayed<br>")
                        return True
                else:
                        print("Blog title not displayed<br>")
                        return False

        def label_to_link_label(self, label):
                link_label = label.lower()
                link_label = re.sub(r'[^\w\s]', '', link_label)
                link_label = link_label.strip()
                link_label = " ".join(link_label.split())
                link_label = link_label.replace(" ", "-")
                return link_label

        def is_blog_link_displayed(self, label):
                link_label = self.label_to_link_label(label)
                link = driver.find_element_by_xpath(self.blog_link.replace("NAME", link_label))
                wait()
                self.scroll_till_label(label)
                wait()
                if link.is_displayed():
                        print("Blog link displayed<br>")
                        return True
                else:
                        print("Blog link not displayed<br>")
                        return False

        def is_blog_image_displayed(self, label):
                link_label = self.label_to_link_label(label)
                img = driver.find_element_by_xpath(self.blog_img.replace("NAME", link_label))
                wait()
                self.scroll_till_label(label)
                wait()
                if img.is_displayed():
                        print("Blog image displayed<br>")
                        return True
                else:
                        print("Blog image not displayed<br>")
                        return False

        def click_blog_title_by_name(self, label):
                title = driver.find_element_by_xpath(self.blog_title.replace("NAME", label))
                wait()
                self.scroll_till_label(label)
                wait()
                try:
                        title.click()
                        print("Blog:" + label + "  clicked<br>")
                except:
                        print("Blog:" + label + "  not clicked<br>")

        def is_blog_view_title_displayed(self, name):
                title = driver.find_element_by_xpath(self.blog_view_title.replace("NAME", name))
                if title.is_displayed():
                        print("Blog title displayed<br>")
                        return True
                else:
                        print("Blog title not displayed<br>")
                        return False

        def is_blog_view_image_displayed(self):
                img = driver.find_element_by_xpath(self.blog_view_banner_img)
                if img.is_displayed():
                        print("Blog image displayed<br>")
                        return True
                else:
                        print("Blog image not displayed<br>")
                        return False

        def is_link_displayed(self, url):
                link = driver.find_element_by_xpath(self.blog_link.replace("NAME", url))
                return link.is_displayed()
                if link.is_displayed():
                        print("Link: " + url + " displayed<br>")
                        return True
                else:
                        print("Link: " + url + " not displayed<br>")
                        return False

        def is_new_blog_button_displayed(self):
                button = driver.find_element_by_xpath(self.new_blog_button)
                if button.is_displayed():
                        print("New Blog button displayed<br>")
                        return True
                else:
                        print("New Blog button not displayed<br>")
                        return False

        def click_new_blog_button(self):
                button = driver.find_element_by_xpath(self.new_blog_button)
                try:
                        button.click()
                        print("New Blog button clicked<br>")
                except:
                        print("New Blog button clicked<br>")

        def click_log_out_button(self):
                button = driver.find_element_by_xpath(
                        self.tag_element.replace("TAG", "button").replace("LABEL", "LOG OUT"))
                try:
                        button.click()
                        print("Log Out button clicked<br>")
                except:
                        print("Log Out button clicked<br>")

        def is_user_logged_in(self):
                try:
                        if self.is_new_blog_button_displayed():
                                print("User is logged in<br>")
                                return True
                        else:
                                print("User not logged in<br>")
                                return False
                except:
                        print("User not logged in<br>")
                        return False

        def login(self, email, pwd):
                self.add_login_details(email, pwd)
                wait()
                self.click_submit_login_button()
                wait(4)
                try:
                        if self.is_login_msg_displayed():
                                print("Logged In Successfully")
                                return True
                except:
                        print("Log in not successful")
                        return False

        def is_log_out_msg_displayed(self):
                msg = driver.find_element_by_xpath(
                        self.tag_element.replace("LABEL", "Successfully logged out.").replace("TAG", "div"))
                try:
                        if msg.is_displayed():
                                print("Log out message  displayed<br>")
                except:
                        print("Log out message not displayed<br>")
                        return False

        def is_unregistered_user_alert_visible(self):
                alert = driver.find_element_by_xpath(self.unregistered_user_alert)
                if alert.is_displayed():
                        print("Unregistered user alert displayed<br>")
                        return True
                else:
                        print("Unregistered user alert not displayed<br>")
                        return False

        def is_new_blog_page_title(self):
                title = driver.find_element_by_xpath(self.new_blog_page_title)
                if title.is_displayed():
                        print("New blog page title displayed<br>")
                        return True
                else:
                        print("New blog page title not displayed<br>")
                        return False

        def is_new_blog_title_input_visible(self):
                ele = driver.find_element_by_xpath(self.new_blog_name_input)
                if ele.is_displayed():
                        print("New blog page title input displayed<br>")
                        return True
                else:
                        print("New blog page title input not displayed<br>")
                        return False

        def is_new_blog_image_input_visible(self):
                ele = driver.find_element_by_xpath(self.new_blog_image_url_input)
                if ele.is_displayed():
                        print("New blog page image input displayed<br>")
                        return True
                else:
                        print("New blog page image input not displayed<br>")
                        return False

        def is_new_blog_textarea_input_visible(self):
                ele = driver.find_element_by_xpath(self.new_blog_input_textarea)
                return ele.is_displayed()
                if ele.is_displayed():
                        print("New blog page textarea input displayed<br>")
                        return True
                else:
                        print("New blog page textarea input not displayed<br>")
                        return False

        def is_new_blog_markdown_preview_visible(self):
                ele = driver.find_element_by_xpath(self.new_blog_input_markdown_preview)
                return ele.is_displayed()
                if ele.is_displayed():
                        print("New blog page markdown preview displayed<br>")
                        return True
                else:
                        print("New blog page markdown preview not displayed<br>")
                        return False

        def verify_toolbar_buttons(self, button):
                toolbar_buttons = self.generate_toolbar_dict()
                button_ele = driver.find_element_by_xpath(toolbar_buttons[button])
                try:
                        if button_ele.is_displayed():
                                print(button + " Button visible<br>")
                                return True
                except:
                        print(button + " Button not visible<br>")
                        return False

        def click_toolbar_button(self, button):
                toolbar_buttons = self.generate_toolbar_dict()
                button_ele = driver.find_element_by_xpath(toolbar_buttons[button])
                try:
                        button_ele.click()
                        print(button + " button clicked<br>")
                except:
                        print(button + " button clicked<br>")

        def go_to_new_blog_page(self):
                ret = False
                if not self.is_user_logged_in():
                        self.click_header_login_button()
                        if 'user/login' in self.get_current_url():
                                ret = True
                        else:
                                ret = False
                        if self.login(self.email_user1, self.pwd_user1):
                                ret = True
                        else:
                                ret = False
                if self.is_new_blog_button_displayed():
                        ret = True
                else:
                        ret = False
                self.click_new_blog_button()
                return ret

        def send_keys_to_editor(self, text):
                textarea = driver.find_element_by_xpath(self.new_blog_input_textarea)
                try:
                        textarea.send_keys(text)
                        print("String sent to editor: " + text + "<br>")
                except:
                        print("String not sent to editor<br>")
                wait(2)

        def clear_text_area(self):
                textarea = driver.find_element_by_xpath(self.new_blog_input_textarea)
                try:
                        textarea.clear()
                        print("Textarea cleared<br>")
                except:
                        print("Textarea not cleared<br>")
                wait(2)

        def get_text_area_contents(self):
                textarea = driver.find_element_by_xpath(self.new_blog_input_textarea)
                print("Text fetched: " + textarea.text + "<br>")
                return textarea.text

        def get_markdown_preview_contents(self, tag=""):
                if tag == "":
                        ele = driver.find_element_by_xpath(self.new_blog_input_markdown_preview + '//p')
                else:
                        mark_down_dict = self.generate_markdown_dict()
                        ele = driver.find_element_by_xpath(mark_down_dict[tag])
                        if tag == 'hr' or tag == "image":
                                if ele.is_displayed():
                                        print(tag + " displayed<br>")
                                        return True
                                else:
                                        print(tag + " not displayed<br>")
                                        return False
                print("Text fetched: " + ele.text + "<br>")
                return ele.text

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

        def set_link_in_textarea(self, text, url):
                wait(1)
                self.click_toolbar_button("link")
                self.send_keys_to_editor(text)
                wait(1)
                get = self.get_text_area_contents()
                self.clear_text_area()
                self.send_keys_to_editor(get.replace("url", url))

        def verify_link_preview_markdown(self, url):
                mark_down_dict = self.generate_markdown_dict()
                ele = driver.find_element_by_xpath(mark_down_dict["link"])
                try:
                        ele.is_displayed()
                except:
                        print("Link not displayed<br>")
                        return False
                if url in ele.get_attribute("href"):
                        print("Link Displayed<br>")
                        return True

        def set_image_in_textarea(self, text, url):
                wait(1)
                self.click_toolbar_button("image")
                self.send_keys_to_editor(url)
                wait(1)
                get = self.get_text_area_contents()
                self.clear_text_area()
                self.send_keys_to_editor(get[:2] + text + get[2:])

        def verify_image_preview_markdown(self, text, url):
                mark_down_dict = self.generate_markdown_dict()
                ele = driver.find_element_by_xpath(mark_down_dict["image"])
                try:
                        ele.is_displayed()
                except:
                        print("Image not displayed<br>")
                        return False
                if url in ele.get_attribute("src") and text in ele.get_attribute("alt"):
                        print("Image displayed<br>")
                        return True

        def set_list_in_textarea(self, type, values):
                wait(1)
                for text in values:
                        self.send_keys_to_editor(text)
                        self.enter()
                self.select_all()
                self.click_toolbar_button(type)
                wait(1)

        def verify_list_preview_markdown(self, type, values):
                mark_down_dict = self.generate_markdown_dict()
                for i in range(len(values)):
                        ele = driver.find_element_by_xpath(mark_down_dict[type + "-element"] + "[" + str(i + 1) + "]")
                        if type == "checked-list":
                                ele1 = driver.find_element_by_xpath(
                                        mark_down_dict[type + "-element"] + "[" + str(i + 1) + "]//input")
                                try:
                                        if ele1.is_displayed(): pass
                                except:
                                        print("List not displayed<br>")
                                        return False
                        if ele.text not in values:
                                print("List not displayed<br>")
                                return False
                print("List displayed<br>")
                return True

        def is_markdown_panes_visible(self, type):
                try:
                        if type == "editor":
                                ele = driver.find_element_by_xpath(self.new_blog_input_textarea)
                        elif type == "preview":
                                ele = driver.find_element_by_xpath(self.new_blog_input_markdown_preview)
                        if ele.is_displayed():
                                print(type + "Pane  displayed<br>")
                                return True
                        else:
                                print(type + "Pane not displayed<br>")
                                return False
                except:
                        print(type + " Pane  not displayed<br>")
                        return False

        def is_editor_fullscreen(self):
                try:
                        ele = driver.find_element_by_xpath(self.new_blog_fullscreen)
                        if ele.is_displayed():
                                print("Editor is fullscreen<br>")
                                return True
                        else:
                                print("Editor is not fullscreen<br>")
                                return False
                except:
                        print("Editor is not fullscreen<br>")
                        return False

        def click_register(self):
                ele = driver.find_element_by_xpath(self.header_links.replace("LINK", "register"))
                wait(1)
                try:
                        ele.click()
                        print("Register button clicked<br>")
                except:
                        print("Register button not clicked<br>")
                wait(2)

        def add_register_details(self, usename, email, pwd):
                uname_input = driver.find_element_by_xpath(self.uname_input)
                email_input = driver.find_element_by_xpath(self.email_input)
                pwd_input = driver.find_element_by_xpath(self.password_input)
                print(
                        "Registration details: <br>Username: " + usename + "<br>Email: " + email + "<br>Password" + pwd + "<br>")
                uname_input.send_keys(usename)
                wait()
                email_input.send_keys(email)
                wait()
                pwd_input.send_keys(pwd)
                wait()

        def verify_admin_page(self, blogs=[]):
                ret = self.is_tag_element_visible("Admin Page", "h1")
                if (len(blogs) > 0):
                        for i in range(len(blogs)):
                                title = driver.find_element_by_xpath(
                                        "(" + self.admin_table_blog_title + ")[" + str(i + 1) + "]")
                                author = driver.find_element_by_xpath(
                                        "(" + self.admin_table_blog_author + ")[" + str(i + 1) + "]")
                                status = driver.find_element_by_xpath(
                                        "(" + self.admin_table_blog_status + ")[" + str(i + 1) + "]")
                                if title.text not in blogs[i][0] or author.text not in blogs[i][1] or status.text not in \
                                        blogs[i][2]:
                                        print("Admin Page Incorrect<br>")
                                        return False
                if ret and True:
                        print("Admin Page Verified<br>")
                else:
                        print("Admin Page Incorrect<br>")
                return ret and True

        def set_new_blog_title_and_image_input(self, title, url):
                ele = driver.find_element_by_xpath(self.new_blog_name_input)
                print("Blog Details: <br>Title: " + title + "<br>Image URL: " + url + "<br>")
                ele.send_keys(title)
                ele = driver.find_element_by_xpath(self.new_blog_image_url_input)
                ele.send_keys(url)

        def approve_blog(self, name):
                ele = driver.find_element_by_xpath(self.approve_button.replace('Title', name))
                try:
                        ele.click()
                        print("Approve Blog Button Clicked<br>")
                except:
                        print("Approve Blog Button Not Clicked<br>")
                wait(2)

        def verify_blog_contents(self, content_dict):
                blog_dict = self.generate_blog_dict()
                for type in content_dict:
                        if type == "Text":
                                ele = self.is_tag_element_visible(content_dict[type], "*")
                                if not ele:
                                        print(type + "content mismatch<br>")
                                        return False
                        elif type == "link":
                                ele = driver.find_element_by_xpath(blog_dict[type])
                                try:
                                        ele.is_displayed()
                                        if content_dict[type][1] not in ele.get_attribute('href') or content_dict[type][
                                                0] not in ele.text:
                                                print(type + "content mismatch<br>")
                                                return False
                                except:
                                        print(type + " not visible<br>")
                                        return False
                        elif type == "image":
                                ele = driver.find_element_by_xpath(blog_dict[type])
                                try:
                                        ele.is_displayed()
                                        if content_dict[type][1] not in ele.get_attribute('src') or content_dict[type][
                                                0] not in ele.get_attribute('alt'):
                                                print(type + " content mismatch<br>")
                                                return False
                                except:
                                        print(type + " not visible<br>")
                                        return False
                        else:
                                ele = driver.find_element_by_xpath(blog_dict[type])
                                try:
                                        ele.is_displayed()
                                        if type not in ele.text:
                                                print(type + " content mismatch<br>")
                                                return False
                                except:
                                        print(type + " not visible<br>")
                                        return False
                        wait(2)
                print("Blog Contents Verified<br>")
                return True
