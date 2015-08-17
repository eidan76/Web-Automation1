author__ = 'Eidan Wasser'
import unittest
import time
from selenium.webdriver.common.by import By
from Utils import InitCase, Config, ClearAllTasks, CreateTaskF

class Daily(unittest.TestCase):

    def test(self):
        InitCase.init_case(menu="ALL", taskNo=0)
        taskID = CreateTaskF.create_a_task("Daily", "Today")
        self.verificationErrors = []

        Config.find_element(Config.taskTitle).click()
        Config.find_element(Config.task_recurrence).click()
        Config.find_element(Config.recurrenceByType, "DAY").click()
        Config.find_element(Config.recurrence_ok).click()
        Config.find_element(Config.task_closeButton).click()
        time.sleep(1)
        Config.find_element(Config.taskCheck).click()
        Config.wait_for_element(Config.taskBySectionName, "Tomorrow")
        taskList = Config.find_elements(Config.task)
        taskList.remove(Config.find_element(Config.taskByID, taskID))

        try: self.assertTrue(Config.is_element_present(Config.taskBySectionName, "Tomorrow"))
        except AssertionError as e: self.verificationErrors.append(str(e))

        try: self.assertTrue(Config.find_element(Config.taskRecurringByID, taskList[0].get_attribute("data-task-id")).is_displayed())
        except AssertionError as e: self.verificationErrors.append(str(e))

        self.assertEqual([], self.verificationErrors)