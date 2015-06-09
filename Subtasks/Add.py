# -*- coding: utf-8 -*-
import unittest
from Utils import Config, InitCase

class Add(unittest.TestCase):
    
    def test(self):
        InitCase.init_case(menu="ALL", taskOption="subtasks")
        self.verificationErrors = []

        Config.find_element(Config.subtasks_newTitle).clear()
        Config.find_element(Config.subtasks_newTitle).send_keys("subtask")
        Config.find_element(Config.subtasks_plusButton).click()

        #Check subtasks badge = 1
        try: self.assertEqual("1", Config.find_element(Config.task_badgeByIconName, "subtasks").get_attribute("data-badge"))
        except AssertionError as e: self.verificationErrors.append(str(e))

        try: self.assertEqual("subtask",  Config.find_element(Config.subtasks_title).text)
        except AssertionError as e: self.verificationErrors.append(str(e))

if __name__ == "__main__":
    unittest.main()
