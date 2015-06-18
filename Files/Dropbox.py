# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from Utils import InitCase, Config

class AddFromDropbox(unittest.TestCase):

    def test(self):
        InitCase.init_case(menu="ALL", taskOption="files")
        driver = Config.get_driver()
        mainWindow = driver.current_window_handle
        self.verificationErrors = []

        Config.find_element(Config.files_dropbox).click()
        dropbox = driver.window_handles
        dropbox.remove(mainWindow)
        driver.switch_to_window(dropbox)

        Config.find_element([By.XPATH, "//input[@name='login_email']"]).clear()
        Config.find_element([By.XPATH, "//input[@name='login_email']"]).send_keys("feedback@any.do")
        Config.find_element([By.XPATH, "//input[@name='login_password']"]).clear()
        Config.find_element([By.XPATH, "//input[@name='login_password']"]).send_keys("itayoni")
        Config.find_element([By.CSS_SELECTOR, "button.login-button.button-primary"]).click()

        Config.wait_for_element([By.XPATH, "//ul[@id='browse-file-list-personal']/li[@data-fqpath=\"/Users\"]"])
        Config.find_element([By.XPATH, "//ul[@id='browse-file-list-personal']/li[@data-fqpath=\"/Users\"]"]).click()
        Config.wait_for_element([By.XPATH, "//ul[@id='browse-file-list-personal']/li[@data-fqpath=\"/Users/Selenium\"]"])
        Config.find_element([By.XPATH, "//ul[@id='browse-file-list-personal']/li[@data-fqpath=\"/Users/Selenium\"]"]).click()
        Config.wait_for_element([By.XPATH, "//ul[@id='browse-file-list-personal']/li[@data-fqpath=\"/Users/Selenium/pic.png\"]"])
        Config.find_element([By.XPATH, "//ul[@id='browse-file-list-personal']/li[@data-fqpath=\"/Users/Selenium/pic.png\"]"]).click()
        Config.find_element([By.ID, "select-btn"]).click()

        driver.switch_to.window(mainWindow)
        try: self.assertEqual("pic.png", Config.find_element(Config.files_name).text)
        except AssertionError as e: self.verificationErrors.append(str(e))

        try: self.assertTrue(Config.is_element_present(Config.files_thumbnailByType, "image"))
        except AssertionError as e: self.verificationErrors.append(str(e))

        #Check files badge = 1
        try: self.assertEqual("1", Config.find_element(Config.task_badgeByIconName, "files").get_attribute("data-badge"))
        except AssertionError as e: self.verificationErrors.append(str(e))

        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
