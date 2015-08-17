__author__ = 'Eidan Wasser'
from Utils import Config
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException
import unittest, time

class FacebookSignIn(unittest.TestCase):
    def test(self):
        driver = Config.get_driver()
        facebook = None
        mainWindow = driver.current_window_handle
        self.verificationErrors = []
        try: Config.wait_for_element_visibility(Config.singUp_FacebookButton, trys=10)
        except :
            if not Config.is_element_present(Config.settingsPane):
                Config.find_element(Config.openSettings).click()
            Config.find_element(Config.settings_profile).click()
            Config.find_element(Config.profile_signOut).click()
            Config.wait_for_element_visibility(Config.singUp_FacebookButton)
        Config.find_element(Config.signIn_alreadyMember).click()
        Config.wait_for_element(Config.signIn_facebook)
        Config.find_element(Config.signIn_facebook).click()

        time.sleep(6)
        try: self.assertFalse(Config.is_element_present(Config.signUp_skipWhatsNew))
        except AssertionError as e: self.verificationErrors.append(str(e))

        Config.wait_for_element(Config.main_hayush)
        try: self.assertEqual("HI RELASE", Config.find_element(Config.main_hayush).text)
        except AssertionError as e: self.verificationErrors.append(str(e))

        try: Config.find_element(Config.profilePic).value_of_css_property("background-image").index("facebook")
        except ValueError as e: self.verificationErrors.append(e)

