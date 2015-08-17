__author__ = 'Eidan Wasser'
# -*- coding: utf-8 -*-
import unittest
from Utils import Config, InitCase
import time

class PriorityHighView(unittest.TestCase):

    def test(self):
        taskID = InitCase.init_case(menu="ALL", view="priority", taskOption="open")
        self.verificationErrors = []

        Config.wait_for_element(Config.task_PrioritySelector)
        Config.find_element(Config.task_PrioritySelector).click()
        time.sleep(2)
        Config.find_element(Config.task_closeButton).click()
        Config.wait_for_element(Config.task_closeButton, present=False)

        try: self.assertEqual(Config.find_element(Config.taskBySectionName, "High").get_attribute("data-task-id"),taskID)
        except AssertionError as e: self.verificationErrors.append(str(e))
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

