# -*- coding: utf-8 -*-
import unittest
import time
from Utils import InitCase, Config

class ChangeList(unittest.TestCase):

    def test(self):
        InitCase.init_case(menu="ALL", taskOption="open")
        self.verificationErrors = []

        Config.find_element(Config.task_FolderSelector).click()
        x = Config.find_element(Config.task_ListSelectorItem).text
        Config.find_element(Config.task_ListSelectorItem).click()

        try: self.assertEqual(x, Config.find_element(Config.task_FolderSelector).text)
        except AssertionError as e: self.verificationErrors.append(str(e))

        Config.find_element(Config.task_closeButton).click()

        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
