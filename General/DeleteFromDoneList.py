# -*- coding: utf-8 -*-
import unittest
import time

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from Utils import ClearAllTasks, Config, InitCase

class DeleteFromDoneListOne(unittest.TestCase):

    def test(self):
        InitCase.init_case(menu="ALL")
        self.verificationErrors = []

        ClearAllTasks.clear_all_tasks()

        Config.find_element(Config.openSettings).click()

        Config.wait_for_element(Config.settings_CompletedTasks)
        Config.find_element(Config.settings_CompletedTasks).click()

        Config.wait_for_element(Config.completedTask)
        Config.find_element(Config.completedTasks_Delete).click()
        Config.wait_for_element_visibility(Config.completedTask, visible=False)

        Config.find_element(Config.overlay).click()
        Config.wait_for_element_visibility(Config.overlay, visible=False)

        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
