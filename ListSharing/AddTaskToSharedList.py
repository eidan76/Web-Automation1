__author__ = 'Eidan Wasser'
import unittest, time, random
from Utils import InitCase, Config, ChangeUser, CreateLoadedTask
from Files import AddNote, AddPic
from General import PriorityHigh
from Subtasks import Add
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class AddTaskToSharedList(unittest.TestCase):
    user = None

    def test(self):
        self.verificationErrors = []

        Config.find_element(Config.openSettings).click()
        time.sleep(1)
        self.user = Config.find_element(Config.settings_email).text

        listID = Config.find_element(Config.main_listByName, "Shared").get_attribute("id")
        InitCase.init_case(menu=listID, taskNo=1)
        CreateLoadedTask.create_loaded_task()

        Config.sync()
        ChangeUser.change_user(self.other_user())
        self.user = self.other_user()

        InitCase.init_case(menu="ALL", taskOption="subtasks")
        try: self.assertEqual("subtask",  Config.find_element(Config.subtasks_title).text)
        except AssertionError as e: self.verificationErrors.append(str(e))

        InitCase.task_options("note")
        try: self.assertTrue(len(Config.find_element(Config.note).text) != 0)
        except AssertionError as e: self.verificationErrors.append(str(e))

        InitCase.task_options("files")
        try: self.assertEqual("2015-03-29.png", Config.find_element(Config.files_name).text)
        except AssertionError as e: self.verificationErrors.append(str(e))

        try: self.assertTrue(Config.is_element_present(Config.files_thumbnailByType, "image"))
        except AssertionError as e: self.verificationErrors.append(str(e))

        InitCase.close_task()
        try: self.assertTrue(Config.is_element_present(Config.taskPriority))
        except AssertionError as e: self.verificationErrors.append(str(e))

        self.assertEqual([], self.verificationErrors)

    def other_user(self):
        u1 = Config.get_receiver()
        u2 = Config.get_sender()
        if self.user == u1:
            return u2
        else:
            return u1