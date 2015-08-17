__author__ = 'Eidan Wasser'
# -*- coding: utf-8 -*-
from selenium.webdriver.common.keys import Keys
import unittest, time, re, NewList
from Utils import Config, InitCase

class EditFromOptions(unittest.TestCase):

    def test(self):
        listID = NewList.listID
        InitCase.init_case(menu=listID, taskNo=None)
        self.verificationErrors = []

        Config.find_element(Config.menuButton).click()
        Config.find_element(Config.menu_editList).click()
        time.sleep(1)
        Config.find_element(Config.listTitleEdit).clear()
        Config.find_element(Config.listTitleEdit).send_keys("a")
        Config.find_element(Config.listTitleEdit).send_keys(Keys.ENTER)
        time.sleep(1)
        try: self.assertEqual("A", Config.find_element(Config.listTitle).text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
