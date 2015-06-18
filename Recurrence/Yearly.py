
__author__ = 'Eidan Wasser'
import unittest
import time, datetime
from selenium.webdriver.common.by import By
from Utils import InitCase, Config, ClearAllTasks

class Yearly(unittest.TestCase):

    def test(self):
        d = datetime.datetime.now()
        dy = d.year + 1
        y = datetime.datetime(dy, d.month, d.day).strftime("%A %m.%d").replace("0","")

        taskID = InitCase.init_case(menu="ALL", taskOption="open", taskNo=1)
        self.verificationErrors = []

        Config.find_element(Config.task_recurrence).click()
        Config.find_element(Config.recurrenceByType, "YEAR").click()
        Config.find_element(Config.recurrence_ok).click()
        Config.find_element(Config.task_closeButton).click()
        time.sleep(1)
        Config.find_element(Config.taskCheck).click()
        Config.wait_for_element(Config.taskBySectionName, "Upcoming")
        taskList = Config.find_elements(Config.task)
        taskList.remove(Config.find_element(Config.taskByID, taskID))

        try: self.assertTrue(Config.is_element_present(Config.taskBySectionName, "Upcoming"))
        except AssertionError as e: self.verificationErrors.append(str(e))

        try: self.assertTrue(Config.find_element(Config.taskRecurringByID, taskList[0].get_attribute("data-task-id")).is_displayed())
        except AssertionError as e: self.verificationErrors.append(str(e))

        Config.find_element(Config.taskTitleBySectionName, "Upcoming").click()

        try: self.assertEqual("Once a year", Config.find_element(Config.task_recurrenceLabel).text)
        except AssertionError as e: self.verificationErrors.append(str(e))

        try: Config.find_element(Config.task_TimeSelector).text.index(y)
        except IndexError as e: self.verificationErrors.append(str(e))

        self.assertEqual([], self.verificationErrors)