import unittest
import  HtmlTestRunner
import os
import  sys
import logging
from pageObjects import  Semicolon,Solvents

class SemiColonTestCases(unittest.TestCase):
        # initialization of website
        def setUp(self):
                self. semicolon = Semicolon()
                self.solvents = Solvents()

        def tearDown(self):
                self.semicolon.close_driver()


        def test_verify_home_page_nonuser(self):
                semicolon=self.semicolon
                solvents = self.solvents
                semicolon.launchsemicolon()

                #*************VERIFYING TEXT LABELS*************
                self.assertTrue(solvents.is_tag_element_visible("Semicolon;",'a'))
                self.assertTrue(solvents.is_tag_element_visible("Express your story.",'p'))
                self.assertTrue(solvents.is_tag_element_visible("Proudly made in India",'p'))
                self.assertTrue(solvents.is_tag_element_visible("Source Code.",'a'))
                self.assertTrue(solvents.is_tag_element_visible("About this project.",'a'))
                self.assertTrue(solvents.is_tag_element_visible("EXPLORE",'p'))
                self.assertTrue(solvents.is_tag_element_visible("REGISTER", 'p'))
                #*************VERIFYING BUTTONS*************'
                self.assertTrue(solvents.is_tag_element_visible("LOGIN;",'button'))
                self.assertTrue(solvents.is_tag_element_visible("Explore",'button'))

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=os.curdir+"/HTML_Reports"))
