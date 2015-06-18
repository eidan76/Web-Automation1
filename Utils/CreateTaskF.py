__author__ = 'Eidan Wasser'
# -*- coding: utf-8 -*-
import time
import unittest
import Config
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def create_a_task(name, section=None):
    taskList = Config.find_elements(Config.task)

    if section == None:
        Config.find_element(Config.list_addTask).click()
    else:
        Config.find_element(Config.list_addTaskToSectionByName, section).click()

    Config.wait_for_element(Config.taskCreate_InputBox)

    Config.find_element(Config.taskCreate_InputBox).clear()
    Config.find_element(Config.taskCreate_InputBox).send_keys(name)
    time.sleep(1)
    Config.find_element(Config.taskCreate_PlusButton).click()
    time.sleep(1)

    newTaskList = Config.find_elements(Config.task)
    for task in taskList:
        newTaskList.remove(task)
    taskID = newTaskList[0].get_attribute("data-task-id")
    return taskID
