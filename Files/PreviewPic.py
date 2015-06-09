# -*- coding: utf-8 -*-
import unittest, time
from Utils import Config, InitCase

class PreviewPic(unittest.TestCase):
    
    def test(self):
        InitCase.init_case(menu="ALL", taskOption="files")
        self.verificationErrors = []

        Config.find_element(Config.files_name).click()

        try: self.assertEqual("true", Config.find_element(Config.files_previewContainer).get_attribute("data-is-image"))
        except AssertionError as e: self.verificationErrors.append(str(e))

        picURL = Config.find_element(Config.files_preview).get_attribute("style")
        try: picURL.index("2015-03-29.png")
        except AssertionError as e: self.verificationErrors.append(str(e))

        Config.find_element(Config.files_previewCloseButton).click()

        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
