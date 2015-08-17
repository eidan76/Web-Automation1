__author__ = 'Eidan Wasser'
import unittest, time, random
from Utils import InitCase, Config, ChangeUser, CreateLoadedTask
from Files import AddNote, AddAudio
from General import PriorityHigh
from Subtasks import Add
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class EditSharedTask(unittest.TestCase):

    def test(self):
        self.verificationErrors = []

        Config.find_element(Config.openSettings).click()
        time.sleep(1)
        user = Config.find_element(Config.settings_email).text

        sender = Config.get_sender()
        receiver = Config.get_receiver()

        InitCase.init_case(menu="ALL")
        CreateLoadedTask.create_loaded_task()
        Config.sync()

        if user == receiver: user = sender
        else: user = receiver
        ChangeUser.change_user(user)

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
