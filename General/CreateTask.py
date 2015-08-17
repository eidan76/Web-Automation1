# -*- coding: utf-8 -*-
import time
import unittest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from Utils import CreateTaskF, InitCase, Config

class CreateATask(unittest.TestCase):

    def test(self):
        InitCase.init_case(menu="ALL", view="date", taskNo=0)
        self.verificationErrors = []

        global taskID
        taskID = CreateTaskF.create_a_task("test", "Today")

        try: self.assertEqual("test", Config.find_element(Config.taskTitleID, taskID).text)
        except AssertionError as e: self.verificationErrors.append(str(e))

        # after test case is complete, all the 'verify' commands that have failed are raised
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
