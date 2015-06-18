__author__ = 'Eidan Wasser'
import unittest
import time, random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from Utils import InitCase, Config, ClearAllTasks

class PriorityView(unittest.TestCase):

    def test(self):
        driver = Config.get_driver()
        self.verificationErrors = []

        listID = Config.find_element(Config.main_listByName, "POS").get_attribute("id")
        taskIDs = InitCase.init_case(menu=listID, view="priority", taskNo=5)

        for i in range(3):
            n = Config.find_element(Config.taskTitleID, random.choice(taskIDs))
            ActionChains(driver).drag_and_drop_by_offset(n, 0, 90).perform()

        Config.find_element(Config.taskTitleID, random.choice(taskIDs)).click()
        Config.wait_for_element(Config.task_PrioritySelectorOff)
        Config.find_element(Config.task_PrioritySelectorOff).click()
        Config.wait_for_element(Config.task_PrioritySelectorOn)
        Config.find_element(Config.task_closeButton).click()
        Config.wait_for_element(Config.task_closeButton, present=False)

        ActionChains(driver).drag_and_drop(Config.find_element(Config.taskTitleBySectionName, "Normal"), Config.find_element(Config.list_sectionByName, "High")).perform()

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
