__author__ = 'Eidan Wasser'
import unittest

from selenium import webdriver

import Signup
from General import General
from Lists import Lists
from Views import Views
from Subtasks import Subtasks
from Files import Files
from Recurrence import Recurrence
from Positioning import Positioning
from Utils import Config, CustomRunner, InitLog



def nsuite():
    n = unittest.TestSuite()
    n.addTest(Signup.SignUp("test"))
    n.addTest(General.general())
    n.addTest(Lists.lists())
    n.addTest(Views.views())
    n.addTest(Subtasks.subtasks())
    n.addTest(Files.files())
    n.addTest(Recurrence.recurrence())
    n.addTest(Positioning.positioning())
    return n

driver = webdriver.Firefox()
Config.set_driver(driver)
driver.implicitly_wait(2)
Config.set_base_url("http://web.any.do")
driver.get(Config.get_base_url())

TestRunName = "Web - General Features"
resultLog = InitLog.init_log(TestRunName)
runner = CustomRunner.Runner(stream=resultLog, resultclass=CustomRunner.Result, runName=TestRunName)
#runner = unittest.TextTestRunner(verbosity=2)
runner.run(nsuite())
resultLog.close()
