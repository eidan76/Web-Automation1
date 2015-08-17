# -*- coding: utf-8 -*-
import unittest
import time
import CreateTask
from selenium.common.exceptions import NoSuchElementException

from Utils import InitCase, Config

class Unswipe(unittest.TestCase):

    def test(self):
        InitCase.init_case(menu="ALL", taskNo=None)
        self.verificationErrors = []

        Config.find_element(Config.taskTitle).click()
        time.sleep(1)
        try: self.assertEqual("unchecked",Config.find_element(Config.task).get_attribute("data-status"))
        except AssertionError as e: self.verificationErrors.append(str(e))

        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
