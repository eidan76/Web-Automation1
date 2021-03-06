# -*- coding: utf-8 -*-
import unittest, time, re
from Utils import InitCase, Config

class DeleteAudio(unittest.TestCase):
    
    def test(self):
        InitCase.init_case(menu="ALL", taskOption="files")
        self.verificationErrors = []

        Config.find_element(Config.files_delete).click()
        Config.find_element(Config.files_deleteConfirm).click()
        time.sleep(3)
        try: self.assertFalse(Config.is_element_present(Config.fileByName, "audio.m4a"))
        except AssertionError as e: self.verificationErrors.append(str(e))

        #Check files badge = 0
        try: self.assertEqual("0", Config.find_element(Config.task_badgeByIconName, "files").get_attribute("data-badge"))
        except AssertionError as e: self.verificationErrors.append(str(e))

        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
