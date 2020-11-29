import unittest
import HtmlTestRunner
import os
from Solvents import Semicolon, Solvents, wait


class SemiColonTestCases(unittest.TestCase):
        semicolon = Semicolon()
        solvents = Solvents()
        email_user1 = 'user1@semicolon.com'
        pwd_user1 = 'semicolon/test'
        def setUp(self):
                self.semicolon.create_driver()
                self.semicolon.launchsemicolon()
        def tearDown(self) :
                self.semicolon.quit()
        @classmethod
        def tearDownClass(cls):
                cls.semicolon.quit()

        def test_verify_home_page_classes(self):
                solvents = self.solvents
                self.assertTrue(solvents.verify_body_and_header_class('banner css-1qk4maf', 'css-8atqhb'))
        def test_verify_home_page_nonuser(self):
                solvents = self.solvents
                # *************VERIFYING TEXT LABELS*************#
                self.assertTrue(solvents.is_tag_element_visible("Semicolon;", 'a'))
                self.assertTrue(solvents.is_tag_element_visible("Express your story.", 'p'))
                self.assertTrue(solvents.is_tag_element_visible("Proudly made in India", 'p'))
                self.assertTrue(solvents.is_tag_element_visible("Source Code.", 'a'))
                self.assertTrue(solvents.is_tag_element_visible("About this project.", 'a'))
                self.assertTrue(solvents.is_tag_element_visible("EXPLORE", 'p'))
                self.assertTrue(solvents.is_tag_element_visible("REGISTER", 'p'))
                # *************VERIFYING BUTTONS*************#
                self.assertTrue(solvents.is_tag_element_visible("Explore", 'button'))
                self.assertTrue(solvents.verify_login_buttons())
                # *************VERIFYING HEADER*************'#
                self.assertTrue(solvents.verify_header_nonuser())
        def test_verify_explore_header_link(self):
                solvents = self.solvents
                solvents.click_header_explore_link()
                self.assertTrue('blogs' in solvents.get_current_url())
        def test_verify_explore_button(self):
                solvents = self.solvents
                solvents.click_button("Explore")
                wait()
                self.assertTrue('blogs' in solvents.get_current_url())
        def test_verify_about_link(self):
                solvents = self.solvents
                solvents.click_link("About this project.")
                wait()
                solvents.switch_to_last_tab()
                self.assertTrue("linkedin" in solvents.get_current_url())
                solvents.switch_to_first_tab()
        def test_verify_source_code_link(self):
                solvents = self.solvents
                solvents.click_link("Source Code.")
                wait()
                solvents.switch_to_last_tab()
                self.assertTrue("github" in solvents.get_current_url())
                solvents.switch_to_first_tab()
        def test_verify_blog_list_explore_page(self):
                solvents = self.solvents
                self.semicolon.launch_blogs_page()
                wait()
                self.assertTrue(solvents.is_blog_page_title_displayed())
                blog_list = ["Getting Started With Machine Learning", "Do your kid needs coding classes ?",
                             "Terms You Should Know Before Getting into Web Development"]
                wait()
                for blog in blog_list:
                        self.assertTrue(solvents.is_blog_title_displayed(blog))
                        self.assertTrue(solvents.is_blog_link_displayed(blog))
                        self.assertTrue(solvents.is_blog_image_displayed(blog))
        def test_verify_blog_page(self):
                solvents = self.solvents
                name = "Getting Started With Machine Learning"
                self.semicolon.launch_blogs_page()
                wait()
                self.assertTrue(solvents.is_blog_page_title_displayed())
                solvents.click_blog_title_by_name(name)
                wait(5)
                self.assertTrue(solvents.is_blog_view_title_displayed(name))
                self.assertTrue(solvents.is_blog_view_image_displayed())
                # *************VERIFYING SHARING LINKS*************#
                self.assertTrue(solvents.is_link_displayed("twitter"))
                self.assertTrue(solvents.is_link_displayed("whatsapp"))
                self.assertTrue(solvents.is_link_displayed("linkedin"))
        def test_verify_login(self):
                solvents = self.solvents
                if solvents.is_user_logged_in():
                        solvents.click_log_out_button()
                solvents.click_header_login_button()
                self.assertTrue('user/login' in solvents.get_current_url())
                self.assertTrue(solvents.login(self.email_user1,self.pwd_user1))
                wait()
        def test_verify_logout_message(self):
                solvents = self.solvents
                if solvents.is_user_logged_in():
                        solvents.click_log_out_button()
                solvents.click_header_login_button()
                self.assertTrue('user/login' in solvents.get_current_url())
                self.assertTrue(solvents.login(self.email_user1, self.pwd_user1))
                solvents.click_log_out_button()
                solvents.is_log_out_msg_displayed()
                wait()
        def test_verify_new_blog_button(self):
                solvents = self.solvents
                if  not solvents.is_user_logged_in():
                        solvents.click_header_login_button()
                        self.assertTrue('user/login' in solvents.get_current_url())
                        self.assertTrue(solvents.login(self.email_user1,self.pwd_user1))
                self.assertTrue(solvents.is_new_blog_button_displayed())
                solvents.click_new_blog_button()
                wait()
                self.assertTrue("/blogs/new" in solvents.get_current_url())
                solvents.click_log_out_button()
        def test_unregistered_user(self):
                solvents = self.solvents
                if solvents.is_user_logged_in():
                        solvents.click_log_out_button()
                solvents.click_header_login_button()
                self.assertTrue('user/login' in solvents.get_current_url())
                wait(2)
                self.assertFalse(solvents.login("user@user.com","password" ))
                self.assertTrue(solvents.is_unregistered_user_alert_visible())
        def test_verify_new_blog_page_structure(self):
                solvents = self.solvents
                if not solvents.is_user_logged_in():
                        solvents.click_header_login_button()
                        self.assertTrue('user/login' in solvents.get_current_url())
                        self.assertTrue(solvents.login(self.email_user1, self.pwd_user1))
                self.assertTrue(solvents.is_new_blog_button_displayed())
                solvents.click_new_blog_button()
                wait()
                self.assertTrue("/blogs/new" in solvents.get_current_url())
                self.assertTrue(solvents.is_new_blog_page_title())
                self.assertTrue(solvents.is_tag_element_visible("Publish","button"))
                self.assertTrue(solvents.is_tag_element_visible("draft","button"))
                self.assertTrue(solvents.is_tag_element_disabled("draft","button"))
        def test_verify_new_blog_input_fields(self):
                solvents = self.solvents
                if not solvents.is_user_logged_in():
                        solvents.click_header_login_button()
                        self.assertTrue('user/login' in solvents.get_current_url())
                        self.assertTrue(solvents.login(self.email_user1, self.pwd_user1))
                self.assertTrue(solvents.is_new_blog_button_displayed())
                solvents.click_new_blog_button()
                wait()
                self.assertTrue("/blogs/new" in solvents.get_current_url())
                self.assertTrue(solvents.is_new_blog_page_title())
                self.assertTrue(solvents.is_new_blog_title_input_visible())
                self.assertTrue(solvents.is_new_blog_image_input_visible())
                self.assertTrue(solvents.is_new_blog_textarea_input_visible())
                self.assertTrue(solvents.is_new_blog_markdown_preview_visible())
        def test_verify_toolbar_button_visible(self):
                solvents = self.solvents
                if not solvents.is_user_logged_in():
                        solvents.click_header_login_button()
                        self.assertTrue('user/login' in solvents.get_current_url())
                        self.assertTrue(solvents.login(self.email_user1, self.pwd_user1))
                self.assertTrue(solvents.is_new_blog_button_displayed())
                solvents.click_new_blog_button()
                wait()
                self.assertTrue("/blogs/new" in solvents.get_current_url())
                buttons = ['bold', 'italic', 'strikethrough', 'hr', 'title', 'link', 'quote', 'code', 'image',
                           'unordered-list', 'ordered-list', 'checked-list', 'edit', 'live', 'preview', 'fullscreen']
                for button in buttons:
                        self.assertTrue(solvents.verify_toolbar_buttons(button))
                wait(2)

if __name__ == '__main__':
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=os.curdir + "/HTML_Reports"))
