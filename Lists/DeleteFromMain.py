__author__ = 'Eidan Wasser'
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, NewList
from Utils import InitCase, Config

class DeleteMain(unittest.TestCase):

    def test(self):
        InitCase.init_case(menu="MAIN")
        self.verificationErrors = []
        listID = NewList.listID

        action = ActionChains(Config.get_driver())
        action.move_to_element(Config.find_element(Config.main_listByID, listID))
        action.click(Config.find_element(Config.main_listOptionsID, listID))
        action.perform()
        time.sleep(1)

        Config.find_element(Config.main_listOptionsID, listID).click()
        Config.find_element(Config.main_listDeleteID, listID).click()
        time.sleep(1)
        Config.find_element(Config.listDeleteConfirm).click()
        try: self.assertFalse(Config.is_element_present(Config.main_listByID, listID))
        except AssertionError as e: self.verificationErrors.append(str(e))
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
