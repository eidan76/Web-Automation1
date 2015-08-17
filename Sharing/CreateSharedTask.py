__author__ = 'Eidan Wasser'
import unittest, time, random
from Utils import InitCase, Config, ChangeUser
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class CreateSharedTask(unittest.TestCase):

    def test(self):
        self.verificationErrors = []
        Config.find_element(Config.openSettings).click()
        time.sleep(1)
        Config.set_sender(Config.find_element(Config.settings_email).text)
        sender = Config.get_sender()
        Config.set_receiver(ChangeUser.change_user())
        receiver = Config.get_receiver()
        ChangeUser.change_user(sender)

        InitCase.init_case(menu="ALL", view="date", taskOption="share")
        Config.find_element(Config.sharing_inputEmail).clear()
        Config.find_element(Config.sharing_inputEmail).send_keys(receiver)
        Config.wait_for_element(Config.sharing_inputEmailDone)
        time.sleep(1)
        Config.find_element(Config.sharing_commitEmailButton).click()
        Config.wait_for_element(Config.sharing_sendInvites)
        Config.find_element(Config.sharing_sendInvites).click()
        Config.wait_for_element(Config.sharing_inviteOverlay, present=False)

        try: self.assertEqual(Config.find_element(Config.sharing_memberBadgeByEmail, receiver).get_attribute("data-status"), "PENDING")
        except AssertionError as e: self.verificationErrors.append(e)

        Config.find_element(Config.sharing_memberBadgeByEmail, receiver).click()
        ActionChains(Config.get_driver()).move_to_element(Config.find_element(Config.sharing_memberPopup)).perform()

        try: self.assertEqual(Config.find_element(Config.sharing_badgeStatus).text, "Invitation sent (Pending)")
        except AssertionError as e:self.verificationErrors.append(e)

        try: self.assertEqual(Config.find_element(Config.sharing_badgeEmail).text, receiver.upper())
        except AssertionError as e: self.verificationErrors.append(e)

        try: self.assertEqual("1", Config.find_element(Config.task_badgeByIconName, "share").get_attribute("data-badge"))
        except AssertionError as e: self.verificationErrors.append(str(e))

        Config.find_element(Config.task_closeButton).click()
        Config.wait_for_element(Config.task_closeButton, present=False)

        try: self.assertTrue(Config.is_element_present(Config.taskSharedAssignee))
        except AssertionError as e: self.verificationErrors.append(str(e))

        ChangeUser.change_user(receiver)

        Config.wait_for_element(Config.sharingInvitation)

        try: self.assertEqual(Config.find_element(Config.sharingInvitation_title).text, "SHARED TASK")
        except AssertionError as e: self.verificationErrors.append(str(e))

        Config.find_element(Config.sharingInvitation_accept).click()
        Config.sync()
        InitCase.init_case(menu="ALL", view="date")

        try: self.assertTrue(Config.find_element(Config.taskShare).is_displayed())
        except AssertionError as e: self.verificationErrors.append(str(e))

        ChangeUser.change_user(sender)
        InitCase.init_case(menu="ALL", taskOption="share")

        try: self.assertEqual(Config.find_element(Config.sharing_memberBadgeByEmail, receiver).get_attribute("data-status"), "ACCEPTED")
        except AssertionError as e: self.verificationErrors.append(e)

        self.assertEqual([], self.verificationErrors)