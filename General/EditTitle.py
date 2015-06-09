# -*- coding: utf-8 -*-
import unittest
import time
from Utils import Config, InitCase
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class EditTitle(unittest.TestCase):

    def test(self):
        InitCase.init_case(menu="ALL")
        self.verificationErrors = []

        Config.find_element(Config.taskTitle).click()
        Config.wait_for_element(Config.task_editTitle)

        Config.find_element(Config.task_editTitle).clear()
        Config.find_element(Config.task_editTitle).send_keys("edited")
        time.sleep(1)

        Config.find_element(Config.task_closeButton).click()
        Config.wait_for_element(Config.task_closeButton, present=False)

        try: self.assertEqual("edited", Config.find_element(Config.taskTitle).text)
        except AssertionError as e: self.verificationErrors.append(str(e))

        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
