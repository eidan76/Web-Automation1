__author__ = 'Eidan Wasser'
# -*- coding: utf-8 -*-
import time
import unittest
import Config
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def create_a_task(name, section):

    Config.find_element(Config.list_addTaskToSectionByName, section).click()

    Config.wait_for_element(Config.taskCreate_InputBox)

    Config.find_element(Config.taskCreate_InputBox).clear()
    Config.find_element(Config.taskCreate_InputBox).send_keys(name)
    time.sleep(1)
    Config.find_element(Config.taskCreate_PlusButton).click()
    time.sleep(1)
    taskID = Config.find_element(Config.taskBySectionName, section).get_attribute("data-task-id")
    return taskID
