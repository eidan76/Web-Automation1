# -*- coding: utf-8 -*-
import unittest, time
from Utils import Config, InitCase

class AddVideo(unittest.TestCase):
    
    def test(self):
        InitCase.init_case(menu="ALL", taskOption="files")
        self.verificationErrors = []

        Config.find_element(Config.files_addFromComputer).send_keys("C:\\Users\\Eidan Wasser\\PycharmProjects\\Suite1\\Files\\vid.mp4")
        Config.wait_for_element(Config.files_progressBar, present=False)

        try: self.assertEqual("vid.mp4", Config.find_element(Config.files_name).text)
        except AssertionError as e: self.verificationErrors.append(str(e))

        try: self.assertTrue(Config.is_element_present(Config.files_thumbnailByType, "video"))
        except AssertionError as e: self.verificationErrors.append(str(e))

        #Check files badge = 1
        try: self.assertEqual("1", Config.find_element(Config.task_badgeByIconName, "files").get_attribute("data-badge"))
        except AssertionError as e: self.verificationErrors.append(str(e))

        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
