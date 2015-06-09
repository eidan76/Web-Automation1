__author__ = 'Eidan Wasser'
# -*- coding: utf-8 -*-
import unittest
from Utils import Config, InitCase

class Delete(unittest.TestCase):

    def test(self):
        InitCase.init_case(menu="ALL", taskOption="subtasks")
        self.verificationErrors = []

        Config.find_element(Config.subtasks_check).click()
        Config.find_element(Config.subtasks_markDone).click()

        #Check badge
        try: self.assertEqual("0", Config.find_element(Config.task_badgeByIconName, "subtasks").get_attribute("data-badge"))
        except AssertionError as e: self.verificationErrors.append(str(e))

        #Check no subtasks present
        try: self.assertFalse(Config.is_element_present(Config.subtask))
        except AssertionError as e: self.verificationErrors.append(str(e))

        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
