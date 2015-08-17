__author__ = 'Eidan Wasser'
import unittest, time
from Utils import CreateTaskF, Config, InitCase

class ChangeDefaultFolder(unittest.TestCase):

    def test(self):
        InitCase.init_case(menu="ALL", taskNo=0)
        self.verificationErrors = []

        Config.find_element(Config.openSettings).click()

        Config.wait_for_element(Config.settings_preferences)
        Config.find_element(Config.settings_preferences).click()
        Config.wait_for_element(Config.preferences_defaultList)
        Config.find_element(Config.preferences_defaultList).click()

        Config.wait_for_element(Config.defaultList_changeDefault)
        newDefaultName = Config.find_element(Config.defaultList_changeDefault).text
        Config.find_element(Config.defaultList_changeDefault).click()

        Config.find_element(Config.overlay).click()
        Config.wait_for_element_visibility(Config.overlay, visible=False)

        CreateTaskF.create_a_task("def")

        Config.find_element(Config.taskTitle).click()
        Config.wait_for_element(Config.task_FolderSelector)

        try: self.assertEqual(Config.find_element(Config.task_FolderSelector).text, newDefaultName)
        except AssertionError as e: self.verificationErrors.append(e)

        self.assertEqual([], self.verificationErrors)