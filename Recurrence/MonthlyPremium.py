__author__ = 'Eidan Wasser'
import unittest
import time, datetime
from selenium.webdriver.common.by import By
from Utils import InitCase, Config, ChangeUser

class MonthlyPremium(unittest.TestCase):

    def test(self):
        d = datetime.datetime.now()
        ChangeUser.change_to_premium()
        taskID = InitCase.init_case(menu="ALL", taskOption="open", taskNo=1)
        self.verificationErrors = []

        Config.find_element(Config.task_recurrence).click()
        Config.find_element(Config.recurrenceByType, "MONTH").click()
        Config.find_element(Config.recurrence_monthlyDayOfWeek).click()
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

        try: self.assertEqual("Once a month, on the " + self.month_by_day(d), Config.find_element(Config.task_recurrenceLabel).text)
        except AssertionError as e: self.verificationErrors.append(str(e))

        try: Config.find_element(Config.task_TimeSelector).text.index(self.next_month_by_day(d))
        except ValueError as e: self.verificationErrors.append(str(e))

        self.assertEqual([], self.verificationErrors)

    def month_by_day(self, d):
        dl = d + datetime.timedelta(7)
        if dl.month != d.month: return "last " + d.strftime("%A")
        x = ((d.day - 1) / 7) + 1
        ordinal = {"1":"first", "2":"second", "3":"third", "4": "fourth", "5": "fifth"}
        return ordinal[str(x)] + " " + d.strftime("%A")

    def next_month_by_day(self,d):
        x = ((d.day - 1) / 7) + 1
        n = d
        while n.month == d.month:
            n += datetime.timedelta(7)
        for i in range(x-1):
            n += datetime.timedelta(7)
        return n.strftime("%A %m.%d").replace("0","")