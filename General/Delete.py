# -*- coding: utf-8 -*-
import unittest
import time
import CreateTask
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from Utils import InitCase, Config

class Delete(unittest.TestCase):

    def test(self):

        InitCase.init_case(menu="ALL")
        self.verificationErrors = []

        Config.find_element(Config.taskCheck).click()
        time.sleep(1)

        for i in range(5):
            try:
                Config.find_element(Config.taskMarkDone).click()
                break
            except: pass
            time.sleep(1)
        else: self.fail("time out")

        try: self.assertFalse(Config.is_element_present(Config.taskByID))
        except AssertionError as e: self.verificationErrors.append(str(e))

        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
