# -*- coding: utf-8 -*-
import unittest
import time
import CreateTask
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from Utils import Config, InitCase


class RestoreFromDeleted(unittest.TestCase):

    def test(self):

        self.verificationErrors = []
        taskID = CreateTask.taskID
        Config.find_element(Config.openSettings).click()

        Config.wait_for_element(Config.settings_CompletedTasks)
        Config.find_element(Config.settings_CompletedTasks).click()

        Config.wait_for_element(Config.completedTask)
        Config.find_element(Config.completedTasks_Restore).click()
        for i in range(5):
            try:
                if "No Completed tasks yet" == Config.find_element(Config.completedTasks_BackgroundText).text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")

        Config.find_element(Config.overlay).click()
        Config.find_element(Config.menu).click()
        Config.find_element(Config.sync).click()
        Config.wait_for_element(Config.taskTitle)

        try: self.assertEqual("edited", Config.find_element(Config.taskTitle).text)
        except AssertionError as e: self.verificationErrors.append(str(e))

        try: self.assertEqual("unchecked", Config.find_element(Config.taskByID, taskID).get_attribute("data-status"))
        except AssertionError as e: self.verificationErrors.append(str(e))

        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
