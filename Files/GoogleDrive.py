# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time
from Utils import Config, InitCase

class GoogleDrive(unittest.TestCase):
    
    def test(self):
        driver = Config.get_driver()
        InitCase.init_case(menu="ALL", taskOption="files")
        mainWindow = driver.current_window_handle
        self.verificationErrors = []
        Config.find_element([By.CSS_SELECTOR, "div.drive-file-input-wrapper"]).click()

        google = driver.window_handles
        google.remove(mainWindow)
        driver.switch_to_window(google)

        driver.find_element_by_id("Email").clear()
        driver.find_element_by_id("Email").send_keys("anydoeidan15@gmail.com")
        driver.find_element_by_id("Passwd").clear()
        driver.find_element_by_id("Passwd").send_keys("mobiitnow")
        driver.find_element_by_id("signIn").click()

        Config.wait_for_element([By.XPATH, "//button[@id=\"submit_approve_access\" and @disabled]"], present=False)
        driver.find_element_by_id("submit_approve_access").click()

        driver.switch_to.window(mainWindow)
        driveFrame = [By.CSS_SELECTOR, "iframe.picker-frame.picker-dialog-frame"]
        Config.wait_for_element(driveFrame, trys=8)
        driver.switch_to.frame(Config.find_element(driveFrame))

        driveFile = [By.XPATH, "//div[@class=\"Nd-ie-te-O-xe-ye\"]"]
        Config.wait_for_element(driveFile)
        Config.find_element(driveFile).click()
        driver.find_element_by_id("picker:ap:0").click()

        driver.switch_to.default_content()
        Config.wait_for_element(Config.files_name)

        try: self.assertEqual("Drive File.xls", Config.find_element(Config.files_name).text)
        except AssertionError as e: self.verificationErrors.append(str(e))

        try: self.assertTrue(Config.is_element_present(Config.files_thumbnailByType, "unknown"))
        except AssertionError as e: self.verificationErrors.append(str(e))

        #Check files badge = 1
        try: self.assertEqual("1", Config.find_element(Config.task_badgeByIconName, "files").get_attribute("data-badge"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
