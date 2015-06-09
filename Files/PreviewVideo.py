# -*- coding: utf-8 -*-
import unittest, time
from Utils import Config, InitCase

class PreviewVideo(unittest.TestCase):

    def test(self):
        InitCase.init_case(menu="ALL", taskOption="files")
        self.verificationErrors = []

        Config.find_element(Config.files_name).click()

        try: self.assertEqual("true", Config.find_element(Config.files_previewContainer).get_attribute("data-is-video"))
        except AssertionError as e: self.verificationErrors.append(str(e))

        videoURL = Config.find_element(Config.files_previewVideo).get_attribute("src")
        try: videoURL.index("vid.mp4")
        except AssertionError as e: self.verificationErrors.append(str(e))

        Config.find_element(Config.files_previewCloseButton).click()

        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
