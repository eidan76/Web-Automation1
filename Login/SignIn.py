__author__ = 'Eidan Wasser'
from Utils import Config, ChangeUser
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import unittest, time

class SignIn(unittest.TestCase):
    def test(self):
        self.verificationErrors = []
        ChangeUser.change_user("autLogin@any.do")

        time.sleep(5)
        try: self.assertFalse(Config.is_element_present(Config.signUp_start))
        except AssertionError as e: self.verificationErrors.append(e)

        Config.wait_for_element(Config.main_hayush)
        try: self.assertEqual(Config.find_element(Config.main_hayush).text, "HI AUTLOGIN")
        except AssertionError as e: self.verificationErrors.append(e)

        Config.find_element(Config.openSettings).click()
        time.sleep(1)
        try: self.assertEqual(Config.find_element(Config.settings_email).text, "autLogin@any.do")
        except AssertionError as e: self.verificationErrors.append(e)