__author__ = 'Eidan Wasser'
# -*- coding: utf-8 -*-
from selenium.webdriver.common.keys import Keys
import unittest, time, NewList
from Utils import InitCase, Config

class EditFromLongPress(unittest.TestCase):

    def test(self):
        listID = NewList.listID
        InitCase.init_case(menu=listID)
        self.verificationErrors = []

        Config.find_element(Config.listTitle).click()
        Config.find_element(Config.listTitleEdit).clear()
        Config.find_element(Config.listTitleEdit).send_keys("z")
        Config.find_element(Config.listTitleEdit).send_keys(Keys.ENTER)
        time.sleep(1)
        try: self.assertEqual("Z", Config.find_element(Config.listTitle).text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
