# -*- coding: utf-8 -*-
import unittest
import datetime

from Utils import InitSuite, Config, InitCase


class Upcoming(unittest.TestCase):
    
    def test(self):
        InitCase.init_case(menu="ALL", view="date")
        self.verificationErrors = []
        taskID = InitSuite.taskID

        Config.find_element(Config.taskTitleID, taskID).click()
        Config.find_element(Config.task_TimeSelector).click()

        #Find what it the selected day in the date selector and select the date 2 days from then
        today = Config.find_element(Config.cal_selectedDay).get_attribute("data-full")
        today = today.split("-")
        today = datetime.date(int(today[0]), int(today[1]) + 1, int(today[2]))
        x = datetime.timedelta(2)
        xDate = today + x
        selectDay = str(xDate.year) + "-" + str(xDate.month - 1) + "-" + str(xDate.day)

        Config.find_element(Config.cal_dayByDate, selectDay).click()
        Config.find_element(Config.cal_OK).click()

        Config.find_element(Config.task_closeButton).click()
        try: self.assertEqual(taskID, Config.find_element(Config.taskBySectionName, "Upcoming").get_attribute("data-task-id"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
