__author__ = 'Eidan Wasser'
# -*- coding: utf-8 -*-
import time
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.common.action_chains import ActionChains
import Config

def clear_all_tasks():
    #Sync
    Config.sync()

    #Check if there are any recurring tasks
    tasks = Config.find_elements(Config.task)
    for t in tasks:
        if Config.find_element(Config.taskRecurringByID, t.get_attribute("data-task-id")).is_displayed():
            Config.find_element(Config.taskTitleID, t.get_attribute("data-task-id")).click()
            Config.find_element(Config.task_recurrence).click()
            Config.find_element(Config.recurrenceByType, "OFF").click()
            Config.find_element(Config.recurrence_ok).click()
            Config.find_element(Config.task_closeButton).click()
            time.sleep(1)

    #Find all check buttons
    activeList = Config.find_elements(Config.taskCheck)
    #If they are available to be pressed (not hidden) press them
    for active in activeList:
        time.sleep(1)
        try: active.click()
        except ElementNotVisibleException: pass

    time.sleep(2)
    delList = Config.find_elements(Config.taskMarkDone)

    for dlt in delList:
        dlt.click()
