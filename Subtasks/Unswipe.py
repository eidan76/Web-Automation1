# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchElementException
import unittest, time
from Utils import InitCase, Config

class Unswipe(unittest.TestCase):
    
    def test(self):
        InitCase.init_case(menu="ALL", taskOption="subtasks")
        self.verificationErrors = []

        Config.find_element(Config.subtasks_title).click()
        time.sleep(1)

        #Check badge
        try: self.assertEqual("1", Config.find_element(Config.task_badgeByIconName, "subtasks").get_attribute("data-badge"))
        except AssertionError as e: self.verificationErrors.append(str(e))

        #Check task status
        try: self.assertEqual("unchecked", Config.find_element(Config.subtask).get_attribute("data-status"))
        except AssertionError as e: self.verificationErrors.append(str(e))

        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
