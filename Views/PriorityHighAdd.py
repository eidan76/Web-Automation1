__author__ = 'Eidan Wasser'
# -*- coding: utf-8 -*-
import unittest
from Utils import ClearAllTasks, CreateTaskF, InitCase, Config

class PriorityHighAdd(unittest.TestCase):

    def test(self):
        InitCase.init_case(menu="ALL", view="priority", taskNo=0)
        self.verificationErrors = []

        taskID = CreateTaskF.create_a_task("priHigh", "High")

        try: self.assertTrue(Config.is_element_present(Config.taskPriority))
        except AssertionError as e: self.verificationErrors.append(str(e))
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

