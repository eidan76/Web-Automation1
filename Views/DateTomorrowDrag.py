# -*- coding: utf-8 -*-
import unittest, time
from selenium.webdriver.common.action_chains import ActionChains

from Utils import InitSuite, Config, InitCase


class DragTomorrow(unittest.TestCase):
    
    def test(self):
        InitCase.init_case(menu="ALL", view="date")
        self.verificationErrors = []
        taskID = InitSuite.taskID

        ActionChains(Config.get_driver()).drag_and_drop(Config.find_element(Config.taskByID, taskID), Config.find_element(Config.list_sectionByName, "Tomorrow")).perform()
        Config.find_element(Config.taskTitleID, taskID).click()

        try: Config.find_element(Config.task_TimeSelector).text.index("Tomorrow")
        except AssertionError as e: self.verificationErrors.append(str(e))

        Config.find_element(Config.task_closeButton).click()
        time.sleep(1)

        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
