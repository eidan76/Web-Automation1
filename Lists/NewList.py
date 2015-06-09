# -*- coding: utf-8 -*-
import unittest, time
from Utils import Config, InitCase
from selenium.webdriver.common.keys import Keys

class NewList(unittest.TestCase):
    
    def test(self):
        InitCase.init_case(menu="MAIN")
        self.verificationErrors = []

        listName = "x"
        Config.find_element(Config.main_newList).click()
        Config.find_element(Config.listTitleEdit).send_keys(listName)
        Config.find_element(Config.listTitleEdit).send_keys(Keys.ENTER)

        try: Config.is_element_present(Config.main_listByName, listName)
        except AssertionError as e: self.verificationErrors.append(str(e))

        global listID
        listID = Config.find_element(Config.main_listByName, listName).get_attribute("id")

        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
