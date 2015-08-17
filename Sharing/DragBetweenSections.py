__author__ = 'Eidan Wasser'
import unittest, time, random
from Utils import InitCase, Config, ChangeUser
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class DragBetweenSections(unittest.TestCase):

    def test(self):
        self.verificationErrors = []

        Config.find_element(Config.openSettings).click()
        time.sleep(1)
        user = Config.find_element(Config.settings_email).text

        InitCase.init_case(menu="ALL", view="date")

        sender = Config.get_sender()
        receiver = Config.get_receiver()

        sections = ["Tomorrow", "Upcoming", "Someday"]
        for i in range(3):
            sec = random.choice(sections)
            ActionChains(Config.get_driver()).drag_and_drop(Config.find_element(Config.task), Config.find_element(Config.list_sectionByName, sec)).perform()
            sections.remove(sec)
            Config.sync()

            if user == receiver: user = sender
            else: user = receiver
            ChangeUser.change_user(user)

            InitCase.init_case(menu="ALL", view="date")
            try: self.assertTrue(Config.is_element_present(Config.taskBySectionName, sec))
            except AssertionError as e: self.verificationErrors.append(str(e))

        self.assertEqual([], self.verificationErrors)