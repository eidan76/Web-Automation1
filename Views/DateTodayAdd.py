__author__ = 'Eidan Wasser'
# -*- coding: utf-8 -*-
import unittest
import time
import datetime
from selenium.common.exceptions import NoSuchElementException

from Utils import ClearAllTasks, InitCase, Config

class TodayAdd(unittest.TestCase):

    def test(self):
        InitCase.init_case(menu="ALL", view="date", taskNo=0)
        self.verificationErrors = []

        #Create task in tomorrow then change date to today from quick add
        Config.find_element(Config.list_addTaskToSectionByName, "Tomorrow").click()
        Config.wait_for_element(Config.task_editTitle)

        Config.find_element(Config.task_editTitle).clear()
        Config.find_element(Config.task_editTitle).send_keys("addToday")

        Config.find_element(Config.task_TimeSelector).click()

        tomorrow = Config.find_element(Config.cal_selectedDay).get_attribute("data-full")
        tomorrow = tomorrow.split("-")
        tomorrow = datetime.date(int(tomorrow[0]), int(tomorrow[1]) + 1, int(tomorrow[2]))
        x = datetime.timedelta(1)
        xDate = tomorrow - x
        today = str(xDate.year) + "-" + str(xDate.month - 1) + "-" + str(xDate.day)

        try: Config.find_element(Config.cal_dayByDate, today).click()
        except NoSuchElementException:
            #move to previous month and try again
            Config.find_element(Config.cal_previousMonth).click()
            Config.find_element(Config.cal_dayByDate, today).click()

        Config.find_element(Config.cal_OK).click()

        time.sleep(1)
        Config.find_element(Config.taskCreate_PlusButton).click()
        time.sleep(1)
        taskName = Config.find_element(Config.taskTitleBySectionName, "Today").text

        try: self.assertEqual(taskName, "addToday")
        except AssertionError as e: self.verificationErrors.append(str(e))

        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

