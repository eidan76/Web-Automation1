__author__ = 'Eidan Wasser'
import unittest, time, random
from Utils import InitCase, Config, ChangeUser
from Files import AddNote, AddPic
from General import PriorityHigh
from Subtasks import Add
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class Comment(unittest.TestCase):

    def test(self):
        self.verificationErrors = []

        Config.find_element(Config.openSettings).click()
        time.sleep(1)
        self.user = Config.find_element(Config.settings_email).text

        InitCase.init_case(menu="ALL", view="date", taskOption="share")

        Config.find_element(Config.sharing_commentInput).clear()
        Config.find_element(Config.sharing_commentInput).send_keys("comment test")
        Config.find_element(Config.sharing_addCommentButton).click()

        Config.sync()
        ChangeUser.change_user(self.other_user())
        self.user = self.other_user()
        InitCase.init_case(menu="ALL", taskOption="share")

        try: self.assertEqual(Config.find_element(Config.sharing_commentAuthor).text + "@any.do", self.other_user())
        except AssertionError as e: self.verificationErrors.append(e)

        try: self.assertEqual(Config.find_element(Config.sharing_commentText).text, "comment test")
        except AssertionError as e: self.verificationErrors.append(e)

        self.assertEqual([], self.verificationErrors)

    def other_user(self):
        u1 = Config.get_receiver()
        u2 = Config.get_sender()
        if self.user == u1:
            return u2
        else:
            return u1