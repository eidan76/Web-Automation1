__author__ = 'Eidan Wasser'
import unittest
from Utils import InitCase, Config

class EditNote(unittest.TestCase):

    def test(self):
        InitCase.init_case(menu="ALL", taskOption="note")
        self.verificationErrors = []
        noteText = "edit edit edit edit"
        Config.find_element(Config.note).send_keys(noteText)

        try: self.assertEqual(" ", Config.find_element(Config.task_badgeByIconName, "notes").get_attribute("data-badge"))
        except AssertionError as e: self.verificationErrors.append(str(e))

        Config.find_element(Config.task_closeButton).click()
        InitCase.task_options("notes")

        try: self.assertEqual(noteText, Config.find_element(Config.task_badgeByIconName, "notes"))
        except AssertionError as e: self.verificationErrors.append(str(e))
