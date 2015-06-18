# -*- coding: utf-8 -*-
import unittest
from selenium.webdriver.common.action_chains import ActionChains

from Utils import Config, InitCase

class PriorityHighDrag(unittest.TestCase):
    
    def test(self):
        taskID = InitCase.init_case(menu="ALL", view="priority")
        self.verificationErrors = []

        ActionChains(Config.get_driver()).drag_and_drop(Config.find_element(Config.taskByID, taskID), Config.find_element(Config.list_sectionByName, "High")).perform()

        try: self.assertTrue(Config.is_element_present(Config.taskPriority))
        except AssertionError as e: self.verificationErrors.append(str(e))

        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
