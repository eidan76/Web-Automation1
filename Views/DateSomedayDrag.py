# -*- coding: utf-8 -*-
import unittest
import time
from selenium.webdriver.common.action_chains import ActionChains
from Utils import InitSuite, Config, InitCase

class DragSomeday(unittest.TestCase):
    
    def test(self):
        InitCase.init_case(menu="ALL", view="date")
        self.verificationErrors = []
        taskID = InitSuite.taskID

        ActionChains(Config.get_driver()).drag_and_drop(Config.find_element(Config.taskByID, taskID), Config.find_element(Config.list_sectionByName, "Someday")).perform()
        Config.find_element(Config.taskTitleID, taskID).click()

        try: Config.find_element(Config.task_TimeSelector).text.index("Someday")
        except AssertionError as e: self.verificationErrors.append(str(e))

        Config.find_element(Config.task_closeButton).click()

        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
