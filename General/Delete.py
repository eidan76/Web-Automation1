# -*- coding: utf-8 -*-
import unittest
import time
import CreateTask
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from Utils import InitCase, Config

class Delete(unittest.TestCase):

    def test(self):

        InitCase.init_case(menu="ALL", taskNo=0)
        self.verificationErrors = []

        try: self.assertFalse(Config.is_element_present(Config.task))
        except AssertionError as e: self.verificationErrors.append(str(e))

        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
