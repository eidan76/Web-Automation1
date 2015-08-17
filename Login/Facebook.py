__author__ = 'Eidan Wasser'
from Utils import Config
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException
import unittest, time

class Facebook(unittest.TestCase):
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
        Config.find_element(Config.singUp_FacebookButton).click()
        try:
            facebook = driver.window_handles
            facebook.remove(mainWindow)
            driver.switch_to_window(facebook)
            time.sleep(4)
            Config.find_element([By.ID, "email"]).clear()
            Config.find_element([By.ID, "email"]).send_keys("eidan+315@any.do")
            Config.find_element([By.ID, "pass"]).clear()
            Config.find_element([By.ID, "pass"]).send_keys("mobiitnow1")
            Config.find_element([By.ID, "loginbutton"]).click()
        except:
            raise FacebookError
        finally:
            driver.switch_to_window(mainWindow)

        Config.wait_for_element(Config.main_hayush, trys=10)
        try: self.assertEqual("HI RELASE", Config.find_element(Config.main_hayush).text)
        except AssertionError as e: self.verificationErrors.append(str(e))

        try: Config.find_element(Config.profilePic).value_of_css_property("background-image").index("facebook")
        except ValueError as e: self.verificationErrors.append(e)

class FacebookError(Exception):
    def __str__(self):
        return "Facebook authentication error"
