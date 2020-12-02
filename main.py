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
                cls.semicolon.delete_blog('Title')
                cls.semicolon.delete_user('user0')
                cls.semicolon.quit()
        #1.
        def test_verify_home_page_classes(self):
                solvents = self.solvents
                print("<strong>Verify Body and Header Class</strong><br>")
                self.assertTrue(solvents.verify_body_and_header_class('banner css-1qk4maf', 'css-8atqhb'))
        #2.
        def test_verify_home_page_nonuser(self):
                solvents = self.solvents
                print("<strong>Verify Text Labels</strong><br>")
                self.assertTrue(solvents.is_tag_element_visible("Semicolon;", 'a'))
                self.assertTrue(solvents.is_tag_element_visible("Express your story.", 'p'))
                self.assertTrue(solvents.is_tag_element_visible("Proudly made in India", 'p'))
                self.assertTrue(solvents.is_tag_element_visible("Source Code.", 'a'))
                self.assertTrue(solvents.is_tag_element_visible("About this project.", 'a'))
                self.assertTrue(solvents.is_tag_element_visible("EXPLORE", 'p'))
                self.assertTrue(solvents.is_tag_element_visible("REGISTER", 'p'))
                print("<strong>Verify Header Buttons</strong><br>")
                self.assertTrue(solvents.is_tag_element_visible("Explore", 'button'))
                self.assertTrue(solvents.verify_login_buttons())
                print("<strong>Verify Header</strong><br>")
                self.assertTrue(solvents.verify_header_nonuser())
        #3.
        def test_verify_explore_header_link(self):
                solvents = self.solvents
                solvents.click_header_explore_link()
                print("<strong>Verify If Blogs Page Is Opened</strong><br>")
                self.assertTrue('blogs' in solvents.get_current_url())
        #4.
        def test_verify_explore_button(self):
                solvents = self.solvents
                solvents.click_button("Explore")
                wait()
                print("<strong>Verify If Blogs Page Is Visited</strong><br>")
                self.assertTrue('blogs' in solvents.get_current_url())
        #5.
        def test_verify_about_link(self):
                solvents = self.solvents
                solvents.click_link("About this project.")
                wait()
                solvents.switch_to_last_tab()
                print("<strong>Verify If LinkedIn Page Is Opened</strong><br>")
                self.assertTrue("linkedin" in solvents.get_current_url())
                solvents.switch_to_first_tab()
        #6.
        def test_verify_source_code_link(self):
                solvents = self.solvents
                solvents.click_link("Source Code.")
                wait()
                solvents.switch_to_last_tab()
                print("<strong>Verify If Github Page Is Opened</strong><br>")
                self.assertTrue("github" in solvents.get_current_url())
                solvents.switch_to_first_tab()
        #7.
        def test_verify_blog_list_explore_page(self):
                solvents = self.solvents
                self.semicolon.launch_blogs_page()
                wait()
                print("<strong>Verify If Blog Page Is Opened</strong><br>")
                self.assertTrue(solvents.is_blog_page_title_displayed())
                blog_list = ["Getting Started With Machine Learning", "Do your kid needs coding classes ?",
                             "Terms You Should Know Before Getting into Web Development"]
                wait()
                for blog in blog_list:
                        print("<strong>Verify Blog List Elements</strong><br>")
                        self.assertTrue(solvents.is_blog_title_displayed(blog))
                        self.assertTrue(solvents.is_blog_link_displayed(blog))
                        self.assertTrue(solvents.is_blog_image_displayed(blog))
        #8.
        def test_verify_blog_page(self):
                solvents = self.solvents
                name = "Getting Started With Machine Learning"
                self.semicolon.launch_blogs_page()
                wait()
                print("<strong>Verify If Blog Page Is Displayed</strong><br>")
                self.assertTrue(solvents.is_blog_page_title_displayed())
                solvents.click_blog_title_by_name(name)
                wait(5)
                print("<strong>Verify Blog Image And Title</strong><br>")
                self.assertTrue(solvents.is_blog_view_title_displayed(name))
                self.assertTrue(solvents.is_blog_view_image_displayed())
                print("<strong>Verify Sharing Links</strong><br>")
                self.assertTrue(solvents.is_link_displayed("twitter"))
                self.assertTrue(solvents.is_link_displayed("whatsapp"))
                self.assertTrue(solvents.is_link_displayed("linkedin"))
        #9.
        def test_verify_login(self):
                solvents = self.solvents
                if solvents.is_user_logged_in():
                        solvents.click_log_out_button()
                solvents.click_header_login_button()
                print("<strong>Verify If Login Page Is Opened</strong><br>")
                self.assertTrue('user/login' in solvents.get_current_url())
                print("<strong>Verify Login</strong><br>")
                self.assertTrue(solvents.login(self.email_user1,self.pwd_user1))
                wait()
        #10.
        def test_verify_logout_message(self):
                solvents = self.solvents
                if solvents.is_user_logged_in():
                        solvents.click_log_out_button()
                solvents.click_header_login_button()
                print("<strong>Verify If Login Page Is Opened</strong><br>")
                self.assertTrue('user/login' in solvents.get_current_url())
                print("<strong>Verify Login</strong><br>")
                self.assertTrue(solvents.login(self.email_user1, self.pwd_user1))
                solvents.click_log_out_button()
                solvents.is_log_out_msg_displayed()
                wait()
        #11.
        def test_verify_new_blog_button(self):
                solvents = self.solvents
                print("<strong>Verify If New Blog Page Is Displayed</strong><br>")
                self.assertTrue(solvents.go_to_new_blog_page())
                wait()
                self.assertTrue("/blogs/new" in solvents.get_current_url())
                solvents.click_log_out_button()
        #12.
        def test_unregistered_user(self):
                solvents = self.solvents
                if solvents.is_user_logged_in():
                        solvents.click_log_out_button()
                solvents.click_header_login_button()
                print("<strong>Verify If Login Page Is Displayed</strong><br>")
                self.assertTrue('user/login' in solvents.get_current_url())
                wait(2)
                print("<strong>Verify Unregistered User Login</strong><br>")
                self.assertFalse(solvents.login("user@user.com","password" ))
                self.assertTrue(solvents.is_unregistered_user_alert_visible())
        #13.
        def test_verify_new_blog_page_structure(self):
                solvents = self.solvents
                self.assertTrue(solvents.go_to_new_blog_page())
                wait()
                print("<strong>Verify If New Blog Page Is Displayed</strong><br>")
                self.assertTrue("/blogs/new" in solvents.get_current_url())
                print("<strong>Verify New Blog Page Elements</strong><br>")
                self.assertTrue(solvents.is_new_blog_page_title())
                self.assertTrue(solvents.is_tag_element_visible("Publish","button"))
                self.assertTrue(solvents.is_tag_element_visible("draft","button"))
                self.assertTrue(solvents.is_tag_element_disabled("draft","button"))
        #14.
        def test_verify_new_blog_input_fields(self):
                solvents = self.solvents
                self.assertTrue(solvents.go_to_new_blog_page())
                wait()
                print("<strong>Verify If New blog Page Is Opened</strong><br>")
                self.assertTrue("/blogs/new" in solvents.get_current_url())
                self.assertTrue(solvents.is_new_blog_page_title())
                print("<strong>Verify Input Fields</strong><br>")
                self.assertTrue(solvents.is_new_blog_title_input_visible())
                self.assertTrue(solvents.is_new_blog_image_input_visible())
                self.assertTrue(solvents.is_new_blog_textarea_input_visible())
                self.assertTrue(solvents.is_new_blog_markdown_preview_visible())
        #15.
        def test_verify_toolbar_button_visible(self):
                solvents = self.solvents
                self.assertTrue(solvents.go_to_new_blog_page())
                wait()
                print("<strong>Verify If New Blog page Is Opened</strong><br>")
                self.assertTrue("/blogs/new" in solvents.get_current_url())
                buttons = ['bold', 'italic', 'strikethrough', 'hr', 'title', 'link', 'quote', 'code', 'image',
                           'unordered-list', 'ordered-list', 'checked-list', 'edit', 'live', 'preview', 'fullscreen']
                for button in buttons:
                        print("<strong>Verify Toolbar Button</strong><br>")
                        self.assertTrue(solvents.verify_toolbar_buttons(button))
                wait(2)
        #16.
        def test_text_formatting_options_preview_toolbar(self):
                solvents = self.solvents
                self.assertTrue(solvents.go_to_new_blog_page())
                wait()
                print("<strong>Verify If New Blog Page Is Displayed</strong><br>")
                self.assertTrue("/blogs/new" in solvents.get_current_url())
                buttons = ['bold', 'italic', 'strikethrough', 'title',  'quote', 'code']
                print("<strong>Verify Plain Text In Preview</strong><br>")
                solvents.send_keys_to_editor("Plain Text")
                self.assertTrue("Plain Text" in solvents.get_markdown_preview_contents())
                for button in buttons:
                        text = button
                        print("<strong>Verify " + text + " In Preview </strong><br>")
                        solvents.clear_text_area()
                        solvents.click_toolbar_button(button)
                        wait(1)
                        solvents.send_keys_to_editor(text)
                        self.assertTrue(text in solvents.get_markdown_preview_contents(button))
                        wait(1)
                wait(2)
        #17.
        def test_verify_horizontal_rule_preview_toolbar(self):
                solvents = self.solvents
                self.assertTrue(solvents.go_to_new_blog_page())
                wait()
                print("<strong>Verify If New Blog Page Is Displayed</strong><br>")
                self.assertTrue("/blogs/new" in solvents.get_current_url())
                solvents.click_toolbar_button("hr")
                wait(2)
                print("<strong>Verify Horizontal Rule</strong><br>")
                self.assertTrue(solvents.get_markdown_preview_contents("hr"))
                wait(2)
        #18.
        def test_verify_link_preview_toolbar(self):
                solvents = self.solvents
                self.assertTrue(solvents.go_to_new_blog_page())
                wait()
                print("<strong>Verify If New Blog Page Is Displayed</strong><br>")
                self.assertTrue("/blogs/new" in solvents.get_current_url())
                solvents.set_link_in_textarea("Link Text","https://www.google.com")
                print("<strong>Verify Link In Markdown Preview</strong><br>")
                self.assertTrue(solvents.verify_link_preview_markdown("https://www.google.com"))
        #19.
        def test_verify_image_preview_toolbar(self):
                solvents = self.solvents
                self.assertTrue(solvents.go_to_new_blog_page())
                wait()
                print("<strong>Verify If New Blog Page Is Displayed</strong><br>")
                self.assertTrue("/blogs/new" in solvents.get_current_url())
                solvents.set_image_in_textarea("Image",
                                               "https://raw.githubusercontent.com/adityavkulkarni/Semicolon_selenium_tests/master/resources/image.jpg")
                wait(1)
                print("<strong>Verify Image In Markdown Preview</strong><br>")
                self.assertTrue(solvents.verify_image_preview_markdown("Image",
                                                                       "https://raw.githubusercontent.com/adityavkulkarni/Semicolon_selenium_tests/master/resources/image.jpg"))
        #20.
        def test_verify_list_preview_toolbar(self):
                solvents = self.solvents
                self.assertTrue(solvents.go_to_new_blog_page())
                wait()
                print("<strong>Verify If New Blog Page Is Displayed</strong><br>")
                self.assertTrue("/blogs/new" in solvents.get_current_url())
                types = ["unordered-list","ordered-list","checked-list"]
                values = ["1","2","3"]
                for type in types:
                        solvents.set_list_in_textarea(type,values)
                        wait(1)
                        print("<strong>Verify "+type+" In Markdown Preview</strong><br>")
                        self.assertTrue(solvents.verify_list_preview_markdown(type,values))
                        solvents.clear_text_area()
        #21.
        def test_verify_preview_options(self):
                solvents = self.solvents
                self.assertTrue(solvents.go_to_new_blog_page())
                wait()
                print("<strong>Verify If New Blog Page Is Displayed</strong><br>")
                self.assertTrue("/blogs/new" in solvents.get_current_url())
                print("<strong>Verify Live Mode</strong><br>")
                solvents.click_toolbar_button("live")
                wait(1)
                self.assertTrue(solvents.is_markdown_panes_visible("editor"))
                wait(1)
                self.assertTrue(solvents.is_markdown_panes_visible("preview"))
                print("<strong>Verify Editor-Only Mode</strong><br>")
                solvents.click_toolbar_button("edit")
                wait(1)
                self.assertTrue(solvents.is_markdown_panes_visible("editor"))
                wait(1)
                self.assertFalse(solvents.is_markdown_panes_visible("preview"))
                print("<strong>Verify Preview-Only Mode</strong><br>")
                solvents.click_toolbar_button("preview")
                wait(1)
                self.assertFalse(solvents.is_markdown_panes_visible("editor"))
                wait(1)
                self.assertTrue(solvents.is_markdown_panes_visible("preview"))
         # 22.
        def test_verify_fullscreen(self):
                solvents = self.solvents
                self.assertTrue(solvents.go_to_new_blog_page())
                wait()
                print("<strong>Verify If New Blog Page Is Displayed</strong><br>")
                self.assertTrue("/blogs/new" in solvents.get_current_url())
                solvents.click_toolbar_button("fullscreen")
                wait(1)
                self.assertTrue(solvents.is_editor_fullscreen())
                solvents.click_toolbar_button("fullscreen")
                wait(1)
                self.assertFalse(solvents.is_editor_fullscreen())
        #23.
        def test_text_formatting_options_preview_md(self):
                solvents = self.solvents
                self.assertTrue(solvents.go_to_new_blog_page())
                wait()
                print("<strong>Verify If New Blog Page Is Displayed</strong><br>")
                self.assertTrue("/blogs/new" in solvents.get_current_url())
                text_formattings = {'bold': '**bold**', 'italic': '*italic*', 'strikethrough': '~~strikethrough~~',
                                    'title': '## title', 'quote': '> quote', 'code': '`code`'}
                print("<strong>Verify Plain Text In Markdown Editor</strong><br>")
                solvents.send_keys_to_editor("Plain Text")
                self.assertTrue("Plain Text" in solvents.get_markdown_preview_contents())
                for function in text_formattings:
                        print("<strong>Verify "+function+" In Markdown Preview</strong><br>")
                        solvents.clear_text_area()
                        wait(1)
                        solvents.send_keys_to_editor(text_formattings[function])
                        self.assertTrue(function in solvents.get_markdown_preview_contents(function))
                        wait(1)
                wait(2)
        #24.
        def test_verify_horizontal_rule_preview_md(self):
                solvents = self.solvents
                self.assertTrue(solvents.go_to_new_blog_page())
                wait()
                print("<strong>Verify If New Blog Page Is Displayed</strong><br>")
                self.assertTrue("/blogs/new" in solvents.get_current_url())
                solvents.send_keys_to_editor("--------------------------------")
                wait(2)
                print("<strong>Verify Horizontal Rule</strong><br>")
                self.assertTrue(solvents.get_markdown_preview_contents("hr"))
                wait(2)
        #25.
        def test_verify_link_preview_md(self):
                solvents = self.solvents
                self.assertTrue(solvents.go_to_new_blog_page())
                wait()
                print("<strong>Verify If New Blog Page Is Displayed</strong><br>")
                self.assertTrue("/blogs/new" in solvents.get_current_url())
                solvents.send_keys_to_editor('[Link Text](https://www.google.com)')
                print("<strong>Verify Link In Markdown Preview</strong><br>")
                self.assertTrue(solvents.verify_link_preview_markdown("https://www.google.com"))
        #26.
        def test_verify_image_preview_md(self):
                solvents = self.solvents
                self.assertTrue(solvents.go_to_new_blog_page())
                wait()
                print("<strong>Verify If New Blog Page Is Displayed</strong><br>")
                self.assertTrue("/blogs/new" in solvents.get_current_url())
                solvents.send_keys_to_editor(
                        '![Image](https://raw.githubusercontent.com/adityavkulkarni/Semicolon_selenium_tests/master/resources/image.jpg)')
                wait(1)
                print("<strong>Verify Image In Markdown Preview</strong><br>")
                self.assertTrue(solvents.verify_image_preview_markdown("Image",
                                                                       "https://raw.githubusercontent.com/adityavkulkarni/Semicolon_selenium_tests/master/resources/image.jpg"))
        #27.
        def test_verify_list_preview_md(self):
                solvents = self.solvents
                self.assertTrue(solvents.go_to_new_blog_page())
                wait()
                print("<strong>Verify If New Blog Page Is Displayed</strong><br>")
                self.assertTrue("/blogs/new" in solvents.get_current_url())
                lists = {"unordered-list":("- 1","- 2","- 3"),
                                "ordered-list":("1. 1","2. 2","3. 3"),
                                "checked-list":("- [ ] 1","- [ ] 2","- [ ] 3")}
                values = ['1','2','3']
                for type in lists:
                        for text in lists[type]:
                                solvents.send_keys_to_editor(text)
                                solvents.enter()
                        wait(1)
                        print("<strong>Verify "+type+" In Markdown Preview</strong><br>")
                        self.assertTrue(solvents.verify_list_preview_markdown(type,values))
                        solvents.clear_text_area()
        #28.
        def test_verify_registration(self):
                solvents = self.solvents
                solvents.click_register()
                self.assertTrue(solvents.is_tag_element_visible("Register.","h2"))
                self.semicolon.launchsemicolon()
                solvents.click_header_login_button()
                solvents.click_register()
                print("<strong>Verify Register Page Is Opened</strong><br>")
                self.assertTrue(solvents.is_tag_element_visible("Register.", "h2"))
                solvents.add_register_details("user0","user0@gmail.com","semicolon/test")
                solvents.click_button("Register")
                wait(2)
                print("<strong>Verify User Is Registered And Logged In</strong><br>")
                self.assertTrue(solvents.is_tag_element_visible("Registerd!","div"))
                self.assertTrue(solvents.is_new_blog_button_displayed())
        #29.
        def test_verify_admin_page(self):
                solvents = self.solvents
                if solvents.is_user_logged_in():
                        solvents.click_log_out_button()
                solvents.click_header_login_button()
                print("<strong>Verify Admin Login</strong><br>")
                self.assertTrue('user/login' in solvents.get_current_url())
                self.assertTrue(solvents.login("admin@semicolon.com", "admin/semicolon"))
                wait()
                print("<strong>Verify Admin Page Login</strong><br>")
                self.assertTrue(solvents.verify_admin_page(
                        [("Getting Started With Machine Learning	", "user1", "true"),
                         ("Do your kid needs coding classes ?	", "user1", "true"),
                         ("Terms You Should Know Before Getting into Web Development	", "user1", "true")]))
                wait(1)
        #30.
        def test_E2E_blog_publish(self):
                solvents = self.solvents
                self.assertTrue(solvents.go_to_new_blog_page())
                wait()
                print("<strong>Verify If New Blog Page Is Displayed</strong><br>")
                self.assertTrue("/blogs/new" in solvents.get_current_url())
                text_formattings = {'bold': '**bold**', 'italic': '*italic*', 'strikethrough': '~~strikethrough~~',
                                    'title': '## title', 'quote': '> quote', 'code': '`code`'}
                print("<strong>Add And Verify Text Format Options</strong><br>")
                solvents.send_keys_to_editor("Plain Text")
                self.assertTrue("Plain Text" in solvents.get_markdown_preview_contents())
                for function in text_formattings:
                        solvents.enter()
                        solvents.enter()
                        wait(1)
                        solvents.send_keys_to_editor(text_formattings[function])
                        self.assertTrue(function in solvents.get_markdown_preview_contents(function))
                        wait(1)
                wait(2)
                solvents.enter()
                solvents.send_keys_to_editor("--------------------------------")
                solvents.enter()
                wait(2)
                solvents.send_keys_to_editor('[Link Text](https://www.google.com)')
                solvents.enter()
                solvents.send_keys_to_editor(
                        '![Image](https://raw.githubusercontent.com/adityavkulkarni/Semicolon_selenium_tests/master/resources/image.jpg)')
                wait(1)
                solvents.set_new_blog_title_and_image_input("Title",
                                                  "https://raw.githubusercontent.com/adityavkulkarni/Semicolon_selenium_tests/master/resources/image.jpg")
                solvents.click_button("Publish")
                wait()
                print("<strong>Verify Blog Published Pop-up</strong><br>")
                self.assertTrue(solvents.is_tag_element_visible("Blog Published!","*"))
                solvents.click_log_out_button()
                self.semicolon.launchsemicolon()
                if solvents.is_user_logged_in():
                        solvents.click_log_out_button()
                solvents.click_header_login_button()
                print("<strong>Verify Admin Login</strong><br>")
                self.assertTrue('user/login' in solvents.get_current_url())
                solvents.login("admin@semicolon.com", "admin/semicolon")
                wait()
                solvents.approve_blog('Title')
                solvents.click_log_out_button()
                if solvents.is_user_logged_in():
                        solvents.click_log_out_button()
                self.semicolon.launchsemicolon()
                solvents.click_header_explore_link()
                blog_list = ["Getting Started With Machine Learning", "Do your kid needs coding classes ?",
                             "Terms You Should Know Before Getting into Web Development",'Title']
                wait()
                for blog in blog_list:
                        print("<strong>Verify Blog Structure For: "+blog+"</strong><br>")
                        self.assertTrue(solvents.is_blog_title_displayed(blog))
                        self.assertTrue(solvents.is_blog_link_displayed(blog))
                        self.assertTrue(solvents.is_blog_image_displayed(blog))
                wait()
                solvents.click_blog_title_by_name('Title')
                self.semicolon.launch_blogs_page()
                wait()
                print("<strong>Verify Blog Page Is Opened</strong><br>")
                self.assertTrue(solvents.is_blog_page_title_displayed())
                solvents.click_blog_title_by_name('Title')
                wait(5)
                self.assertTrue(solvents.is_blog_view_title_displayed('Title'))
                self.assertTrue(solvents.is_blog_view_image_displayed())
                print("<strong>Verify Sharing Links</strong><br>")
                self.assertTrue(solvents.is_link_displayed("twitter"))
                self.assertTrue(solvents.is_link_displayed("whatsapp"))
                self.assertTrue(solvents.is_link_displayed("linkedin"))
                content_dict = {
                        "Text": "Plain Text",
                        'bold': 'bold', 'italic': 'italic', 'strikethrough': 'strikethrough',
                        'title': 'title', 'quote': ' quote', 'code': 'code',
                        "link": ('Link Text', 'https://www.google.com'),
                        "image": ('Image',
                          'https://raw.githubusercontent.com/adityavkulkarni/Semicolon_selenium_tests/master/resources/image.jpg')
                }
                print("<strong>Verify Blog Content</strong><br>")
                self.assertTrue(solvents.verify_blog_contents(content_dict))
if __name__ == '__main__':
        #unittest.main()
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=os.curdir + "/HTML_Reports"))
