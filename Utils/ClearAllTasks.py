__author__ = 'Eidan Wasser'
# -*- coding: utf-8 -*-
import time
from selenium.common.exceptions import ElementNotVisibleException
import Config

def clear_all_tasks():

    #Find all check buttons
    activeList = Config.find_elements(Config.taskCheck)

    #If they are available to be pressed (not hidden) press them
    for active in activeList:
        try: active.click()
        except ElementNotVisibleException: pass

    time.sleep(2)
    delList = Config.find_elements(Config.taskMarkDone)

    for dlt in delList:
        dlt.click()
