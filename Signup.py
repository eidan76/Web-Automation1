# -*- coding: utf-8 -*-
import unittest
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from Utils import Config

class SignUp(unittest.TestCase):

    def test(self):
        self.verificationErrors = []
        date = str(time.time())
        Config.wait_for_element(Config.signUp_emailButton)

        Config.find_element(Config.signUp_emailButton).click()
        Config.wait_for_element(Config.signUp_inputName)
        Config.find_element(Config.signUp_inputName).clear()
        Config.find_element(Config.signUp_inputName).send_keys(date)
        Config.find_element(Config.signUp_inputEmail).clear()
        Config.find_element(Config.signUp_inputEmail).send_keys(date, "@any.do")
        Config.find_element(Config.signUp_inputPass).clear()
        Config.find_element(Config.signUp_inputPass).send_keys("123456")
        Config.find_element(Config.signUp_RegisterButton).click()
        time.sleep(1)

        self.assertEqual("", Config.find_element(Config.signUp_ErrorMessage).text)
        Config.wait_for_element(Config.signUp_start)
        Config.find_element(Config.signUp_start).click()

        try: self.assertEqual("HI " + date, Config.find_element(Config.main_hayush).text)
        except AssertionError as e: self.verificationErrors.append(str(e))

        # after test case is complete, all the 'verify' commands that have failed are raised
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
