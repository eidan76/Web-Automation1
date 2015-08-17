__author__ = 'Eidan Wasser'
# -*- coding: utf-8 -*-
import unittest, time

from Utils import Config, InitCase

class PriorityNormalView(unittest.TestCase):

    def test(self):
        taskID = InitCase.init_case(menu="ALL", view="priority")
        self.verificationErrors = []

        Config.find_element(Config.taskTitle).click()

        Config.wait_for_element(Config.task_PrioritySelector)
        Config.find_element(Config.task_PrioritySelector).click()
        time.sleep(1)

        Config.find_element(Config.task_closeButton).click()
        Config.wait_for_element(Config.task_closeButton, present=False)

        try: self.assertEqual(Config.find_element(Config.taskBySectionName, "Normal").get_attribute("data-task-id"), taskID)
        except AssertionError as e: self.verificationErrors.append(str(e))
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

