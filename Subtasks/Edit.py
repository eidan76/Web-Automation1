__author__ = 'Eidan Wasser'
# -*- coding: utf-8 -*-
from selenium.webdriver.common.keys import Keys
import unittest, time
from Utils import Config, InitCase

class Edit(unittest.TestCase):

    def test(self):
        InitCase.init_case(menu="ALL", taskOption="subtasks")
        self.verificationErrors = []

        Config.find_element(Config.subtasks_title).click()
        Config.find_element(Config.subtasks_title).clear()
        Config.find_element(Config.subtasks_title).send_keys("edited")
        Config.find_element(Config.task_badgeByIconName, "subtasks").click()

        try: self.assertEqual("edited",  Config.find_element(Config.subtasks_title).text)
        except AssertionError as e: self.verificationErrors.append(str(e))

if __name__ == "__main__":
    unittest.main()
