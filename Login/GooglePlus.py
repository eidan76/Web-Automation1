__author__ = 'Eidan Wasser'
from Utils import Config
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException, NoSuchWindowException
import unittest, time

class GooglePlus(unittest.TestCase):
    def test(self):
        driver = Config.get_driver()
        google = None
        mainWindow = driver.current_window_handle
        self.verificationErrors = []
        try: Config.wait_for_element_visibility(Config.singUp_GooglePlusButton, trys=10)
        except ElementNotVisibleException:
            if not Config.is_element_present(Config.settingsPane):
                Config.find_element(Config.openSettings).click()
            Config.find_element(Config.settings_profile).click()
            Config.find_element(Config.profile_signOut).click()
            Config.wait_for_element_visibility(Config.singUp_GooglePlusButton)
        Config.find_element(Config.singUp_GooglePlusButton).click()
        try:
            google = driver.window_handles
            google.remove(mainWindow)
            driver.switch_to_window(google)

            Config.wait_for_element([By.ID, "Email"])
            Config.find_element([By.ID, "Email"]).clear()
            Config.find_element([By.ID, "Email"]).send_keys("anydoeidan15@gmail.com")
            if Config.is_element_present([By.ID, "Passwd"]) == False:
                Config.find_element([By.ID, "next"]).click()
                Config.wait_for_element([By.CSS_SELECTOR, "input#Passwd"])
            Config.find_element([By.CSS_SELECTOR, "input#Passwd"]).clear()
            Config.find_element([By.CSS_SELECTOR, "input#Passwd"]).send_keys("mobiitnow")
            Config.find_element([By.ID, "signIn"]).click()
            time.sleep(3)
            if Config.is_element_present([By.XPATH, "//button[@id=\"submit_approve_access\"]"]):
                Config.wait_for_element([By.XPATH, "//button[@id=\"submit_approve_access\" and @disabled]"], present=False)
                Config.find_element([By.ID, "submit_approve_access"]).click()
        except NoSuchWindowException:
            driver.switch_to_window(mainWindow)
        except: self.verificationErrors.append("Google authentication error")
        else: driver.switch_to_window(mainWindow)

        try:
            Config.wait_for_element([By.CSS_SELECTOR, "div#skip.textButton"])
            Config.find_element([By.CSS_SELECTOR, "div#skip.textButton"]).click()
        except: pass
        Config.wait_for_element(Config.main_hayush)
        try: self.assertEqual("HI ANY", Config.find_element(Config.main_hayush).text)
        except AssertionError as e: self.verificationErrors.append(str(e))

        try: Config.find_element(Config.profilePic).value_of_css_property("background-image").index("google")
        except ValueError as e: self.verificationErrors.append(e)

