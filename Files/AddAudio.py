__author__ = 'Eidan Wasser'
# -*- coding: utf-8 -*-
import unittest, time
from selenium.webdriver.common.by import By
from Utils import Config, InitCase

class AddAudio(unittest.TestCase):

    def test(self):
        InitCase.init_case(menu="ALL", taskOption="files")
        self.verificationErrors = []

        Config.find_element(Config.files_addFromComputer).send_keys("C:\\Users\\Eidan Wasser\\PycharmProjects\\Suite1\\Files\\audio.m4a")
        Config.wait_for_element(Config.files_progressBar, present=False)

        try: self.assertTrue(Config.is_element_present(Config.files_thumbnailByType, "audio"))
        except AssertionError as e: self.verificationErrors.append(str(e))

        try: self.assertTrue(Config.is_element_present([By.CSS_SELECTOR, "audio"]))
        except AssertionError as e: self.verificationErrors.append(str(e))

        #Check files badge = 1
        try: self.assertEqual("1", Config.find_element(Config.task_badgeByIconName, "files").get_attribute("data-badge"))
        except AssertionError as e: self.verificationErrors.append(str(e))

        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
