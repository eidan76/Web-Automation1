__author__ = 'Eidan Wasser'
import unittest
import time, random, datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from Utils import InitCase, Config, ClearAllTasks

class DateView(unittest.TestCase):

    def test(self):
        driver = Config.get_driver()
        self.verificationErrors = []

        listID = Config.find_element(Config.main_listByName, "POS").get_attribute("id")
        taskIDs = InitCase.init_case(menu=listID, view="date", taskNo=5)

        for i in range(3):
            n = Config.find_element(Config.taskTitleID, random.choice(taskIDs))
            ActionChains(driver).drag_and_drop_by_offset(n, 0, 90).perform()

        Config.find_element(Config.taskTitleID, random.choice(taskIDs)).click()
        Config.wait_for_element(Config.task_TimeSelector)
        Config.find_element(Config.task_TimeSelector).click()

        selectDay = self.select_day(Config.find_element(Config.cal_selectedDay).get_attribute("data-full"))
        Config.find_element(Config.cal_dayByDate, selectDay).click()
        Config.find_element(Config.cal_OK).click()

        Config.find_element(Config.task_closeButton).click()
        Config.wait_for_element(Config.task_closeButton, present=False)

        ActionChains(driver).drag_and_drop(Config.find_element(Config.taskTitleBySectionName, "Today"), Config.find_element(Config.list_sectionByName, "Upcoming")).perform()

        InitCase.select_view("clean")
        newOrder = Config.find_elements(Config.task)
        newOrderIDs = []
        for t in newOrder:
            newOrderIDs.append(t.get_attribute("data-task-id"))

        mainWindow = driver.current_window_handle
        driver.execute_script("$(window.open())")
        window2 = driver.window_handles
        window2.remove(mainWindow)
        driver.switch_to_window(window2)
        driver.get(Config.get_base_url())

        InitCase.init_case(menu=listID, view="clean", taskNo=5)

        platform2Order = Config.find_elements(Config.task)

        for t in range(len(platform2Order)):
            try: self.assertEqual(platform2Order[t].get_attribute("data-task-id"), newOrderIDs[t])
            except AssertionError as e: self.verificationErrors.append(str(e))

        driver.close()
        driver.switch_to_window(mainWindow)

    def select_day(self, today):
        Config.find_element(Config.cal_selectedDay).get_attribute("data-full")
        today = today.split("-")
        today = datetime.date(int(today[0]), int(today[1]) + 1, int(today[2]))
        x = datetime.timedelta(2)
        xDate = today + x
        return str(xDate.year) + "-" + str(xDate.month - 1) + "-" + str(xDate.day)
