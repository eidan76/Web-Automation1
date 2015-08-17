__author__ = 'Eidan Wasser'
import unittest, time, random
from Utils import InitCase, Config, ChangeUser
from Lists import DeleteFromOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class CreateSharedList(unittest.TestCase):

    def test(self):
        self.verificationErrors = []
        ChangeUser.change_to_premium()
        Config.find_element(Config.openSettings).click()
        time.sleep(1)
        Config.set_sender(Config.find_element(Config.settings_email).text)
        sender = Config.get_sender()
        Config.set_receiver(ChangeUser.change_user())
        receiver = Config.get_receiver()
        ChangeUser.change_user(sender)

        InitCase.init_case(menu="MAIN")
        while Config.is_element_present(Config.main_listByName, "Shared"):
            xl = DeleteFromOptions.DeleteFromOptions("test")
            xl.test(Config.find_element(Config.main_listByName, "Shared").get_attribute("id"))

        Config.find_element(Config.main_newList).click()
        Config.find_element(Config.listTitleEdit).send_keys("Shared")
        Config.find_element(Config.listTitleEdit).send_keys(Keys.ENTER)

        listID = Config.find_element(Config.main_listByName, "Shared").get_attribute("id")
        Config.find_element(Config.main_listByName, "Shared").click()

        Config.find_element(Config.list_addSharedMemberButton).click()
        Config.find_element(Config.sharing_inputEmail).clear()
        Config.find_element(Config.sharing_inputEmail).send_keys(receiver)
        Config.wait_for_element(Config.sharing_commitEmailButton)
        time.sleep(1)
        Config.find_element(Config.sharing_commitEmailButton).click()
        Config.wait_for_element(Config.sharing_sendInvites)
        Config.find_element(Config.sharing_sendInvites).click()
        Config.wait_for_element(Config.sharing_sendInvites, present=False)

        time.sleep(1)
        try: self.assertEqual(Config.find_element(Config.sharing_memberBadgeByEmail, receiver).get_attribute("data-status"), "PENDING")
        except AssertionError as e: self.verificationErrors.append(e)

        Config.find_element(Config.sharing_memberBadgeByEmail, receiver).click()
        ActionChains(Config.get_driver()).move_to_element(Config.find_element(Config.sharing_memberPopup)).perform()
        time.sleep(1)
        try: self.assertEqual(Config.find_element(Config.sharing_badgeStatus).text, "Invitation sent (Pending)")
        except AssertionError as e:self.verificationErrors.append(e)

        try: self.assertEqual(Config.find_element(Config.sharing_badgeEmail).text, receiver.upper())
        except AssertionError as e: self.verificationErrors.append(e)

        Config.find_element(Config.task_closeButton).click()
        Config.wait_for_element(Config.task_closeButton, present=False)

        try: self.assertEqual(Config.find_element(Config.list_sharedMemberByEmail, receiver).get_attribute("data-status"), "PENDING")
        except AssertionError as e: self.verificationErrors.append(e)

        Config.find_element(Config.goToMainGrid).click()
        try: self.assertEqual(Config.find_element(Config.main_sharedListMembersByListID, listID).get_attribute("data-status"), "PENDING")
        except AssertionError as e: self.verificationErrors.append(e)

        ChangeUser.change_user(receiver)

        Config.wait_for_element(Config.sharingInvitation)

        try: self.assertEqual(Config.find_element(Config.sharingInvitation_title).text, "SHARED LIST")
        except AssertionError as e: self.verificationErrors.append(str(e))

        Config.find_element(Config.sharingInvitation_accept).click()
        Config.sync()
        InitCase.init_case(menu="MAIN")

        try: self.assertEqual(Config.find_element(Config.sharing_memberBadgeByEmail, sender).get_attribute("data-status"), "CREATOR")
        except AssertionError as e: self.verificationErrors.append(e)

        ChangeUser.change_user(sender)
        InitCase.init_case(menu="MAIN")

        try: self.assertEqual(Config.find_element(Config.sharing_memberBadgeByEmail, receiver).get_attribute("data-status"), "ACCEPTED")
        except AssertionError as e: self.verificationErrors.append(e)

        self.assertEqual([], self.verificationErrors)

    def get_list(self, old_lists, new_lists):
        for i in new_lists:
            if i in old_lists:
                new_lists.remove(i)
        return new_lists[0]