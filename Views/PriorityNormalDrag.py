# -*- coding: utf-8 -*-
import unittest
from selenium.webdriver.common.action_chains import ActionChains

from Utils import InitSuite, Config, InitCase


class PriorityNormalDrag(unittest.TestCase):
    
    def test(self):
        InitCase.init_case(menu="ALL", view="priority")
        self.verificationErrors = []
        taskID = InitSuite.taskID

        ActionChains(Config.get_driver()).drag_and_drop(Config.find_element(Config.taskByID, taskID), Config.find_element(Config.list_sectionByName, "Normal")).perform()

        try: self.assertFalse(Config.is_element_present(Config.taskPriority))
        except AssertionError as e: self.verificationErrors.append(str(e))

        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
