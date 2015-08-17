__author__ = 'Eidan Wasser'
import unittest, time, random
from Utils import InitCase, Config, ChangeUser
from selenium.webdriver.common.action_chains import ActionChains

class Decline(unittest.TestCase):
    user = None

    def test(self):
        self.verificationErrors = []

        Config.find_element(Config.openSettings).click()
        time.sleep(1)
        self.user = Config.find_element(Config.settings_email).text

        InitCase.init_case(menu="ALL", taskNo=0)
        InitCase.init_case(menu="ALL", view="date", taskOption="share")
        Config.find_element(Config.sharing_inputEmail).clear()
        Config.find_element(Config.sharing_inputEmail).send_keys(self.other_user())
        Config.wait_for_element(Config.sharing_inputEmailDone)
        time.sleep(1)
        Config.find_element(Config.sharing_commitEmailButton).click()
        Config.wait_for_element(Config.sharing_sendInvites)
        Config.find_element(Config.sharing_sendInvites).click()
        Config.wait_for_element(Config.sharing_inviteOverlay, present=False)

        ChangeUser.change_user(self.other_user())
        self.user = self.other_user()

        Config.wait_for_element(Config.sharingInvitation)

        try: self.assertEqual(Config.find_element(Config.sharingInvitation_title).text, "SHARED TASK")
        except AssertionError as e: self.verificationErrors.append(str(e))

        Config.find_element(Config.sharingInvitation_decline).click()
        Config.sync()
        InitCase.select_menu("ALL")

        try: self.assertFalse(Config.find_element(Config.taskShare).is_displayed())
        except AssertionError as e: self.verificationErrors.append(str(e))

        ChangeUser.change_user(self.other_user())
        self.user = self.other_user()

        InitCase.init_case(menu="ALL", taskOption="share")

        try: self.assertEqual(Config.find_element(Config.sharing_memberBadgeByEmail, self.other_user()).get_attribute("data-status"), "REJECTED")
        except AssertionError as e: self.verificationErrors.append(e)

        Config.find_element(Config.sharing_memberBadgeByEmail, self.other_user()).click()
        ActionChains(Config.get_driver()).move_to_element(Config.find_element(Config.sharing_memberPopup)).perform()

        try: self.assertEqual(Config.find_element(Config.sharing_badgeStatus).text, "Rejected Invitation")
        except AssertionError as e: self.verificationErrors.append(e)

        self.assertEqual([], self.verificationErrors)

    def other_user(self):
        u1 = Config.get_receiver()
        u2 = Config.get_sender()
        if self.user == u1:
            return u2
        else:
            return u1