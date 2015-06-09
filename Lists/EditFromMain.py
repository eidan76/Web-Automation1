# -*- coding: utf-8 -*-
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import unittest, time, re, NewList
from Utils import Config, InitCase


class EditMain(unittest.TestCase):
    
    def test(self):
        InitCase.init_case(menu="MAIN")
        self.verificationErrors = []
        listID = NewList.listID

        ActionChains(Config.get_driver()).move_to_element(Config.find_element(Config.main_listByID, listID)).perform()
        time.sleep(1)

        Config.find_element(Config.main_listOptionsID, listID).click()
        Config.find_element(Config.main_listEditID, listID).click()
        Config.find_element(Config.listTitleEdit).clear()
        Config.find_element(Config.listTitleEdit).send_keys("y")
        Config.find_element(Config.listTitleEdit).send_keys(Keys.ENTER)
        time.sleep(1)
        try: self.assertEqual("Y", Config.find_element(Config.main_ListNameID, listID).text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
