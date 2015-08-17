# -*- coding: utf-8 -*-
import unittest
import time
from Utils import InitCase, Config, ChangeUser

class ChangeFromSharedList(unittest.TestCase):

    def test(self):
        Config.find_element(Config.openSettings).click()
        time.sleep(1)
        self.user = Config.find_element(Config.settings_email).text

        listID = Config.find_element(Config.main_listByName, "Shared").get_attribute("id")
        InitCase.init_case(menu=listID, taskNo=1, taskOption="open")
        self.verificationErrors = []

        Config.find_element(Config.task_FolderSelector).click()
        Config.find_element(Config.task_ListSelectorItem).click()

        Config.find_element(Config.task_closeButton).click()
        Config.sync()

        ChangeUser.change_user(self.other_user())
        self.user = self.other_user()

        Config.find_element(Config.main_listByName, "Shared").click()

        try: self.assertFalse(Config.is_element_present(Config.task))
        except AssertionError as e: self.verificationErrors.append(str(e))

        self.assertEqual([], self.verificationErrors)

    def other_user(self):
        u1 = Config.get_receiver()
        u2 = Config.get_sender()
        if self.user == u1:
            return u2
        else:
            return u1