__author__ = 'Eidan Wasser'
import unittest
from Utils import ClearAllTasks, CreateTaskF, InitCase

class InitSuite(unittest.TestCase):

    def test(self):
        InitCase.init_case(menu="ALL", view="date")
        self.verificationErrors = []

        ClearAllTasks.clear_all_tasks()
        global taskID
        taskID = CreateTaskF.create_a_task("test", "Today")
