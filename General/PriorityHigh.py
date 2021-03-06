# -*- coding: utf-8 -*-
import unittest
import time

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from Utils import Config, InitCase

class PriorityHigh(unittest.TestCase):

    def test(self):
        InitCase.init_case(menu="ALL", taskOption="open")
        self.verificationErrors = []

        Config.wait_for_element(Config.task_PrioritySelector)
        Config.find_element(Config.task_PrioritySelector).click()
        time.sleep(2)
        Config.find_element(Config.task_closeButton).click()
        Config.wait_for_element(Config.task_closeButton, present=False)

        try: self.assertTrue(Config.is_element_present(Config.taskPriority))
        except AssertionError as e: self.verificationErrors.append(str(e))

        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
