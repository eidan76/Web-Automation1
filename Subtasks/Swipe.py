__author__ = 'Eidan Wasser'
import unittest, time
from selenium.webdriver.common.action_chains import ActionChains
from Utils import InitCase, Config

class Swipe(unittest.TestCase):

    def test(self):
        InitCase.init_case(menu="ALL", taskOption="subtasks")
        self.verificationErrors = []
        ActionChains(Config.get_driver()).move_to_element(Config.find_element(Config.subtask)).perform()
        time.sleep(1)
        Config.find_element(Config.subtasks_check).click()
        time.sleep(1)
        #Check badge
        try: self.assertEqual("0", Config.find_element(Config.task_badgeByIconName, "subtasks").get_attribute("data-badge"))
        except AssertionError as e: self.verificationErrors.append(str(e))

        #Check task status
        try: self.assertEqual("checked", Config.find_element(Config.subtask).get_attribute("data-status"))
        except AssertionError as e: self.verificationErrors.append(str(e))

        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
