# -*- coding: utf-8 -*-
__author__ = 'Eidan Wasser'
import unittest
import time
from selenium.webdriver.common.action_chains import ActionChains
from Utils import Config, InitCase

class DragSomeday(unittest.TestCase):

    def test(self):
        self.verificationErrors = []
        taskID = InitCase.init_case(menu="ALL", view="date", taskOption="open", taskNo=1)

        Config.find_element(Config.task_recurrence).click()
        Config.find_element(Config.recurrenceByType, "DAY").click()
        Config.find_element(Config.recurrence_ok).click()
        Config.find_element(Config.task_closeButton).click()
        time.sleep(1)
        ActionChains(Config.get_driver()).drag_and_drop(Config.find_element(Config.taskByID, taskID), Config.find_element(Config.list_sectionByName, "Someday")).perform()

        Config.find_element(Config.taskTitleID, taskID).click()
        try: self.assertEqual("", Config.find_element(Config.task_recurrenceLabel).text)
        except AssertionError as e: self.verificationErrors.append(str(e))

        Config.find_element(Config.task_closeButton).click()

        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

