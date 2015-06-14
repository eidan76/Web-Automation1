__author__ = 'Eidan Wasser'
import unittest

from selenium import webdriver

import Signup
from General import General
from Lists import Lists
from Views import Views
from Subtasks import Subtasks
from Files import Files

from Utils.Config import set_driver
from Utils import InitLog, CustomRunner

def nsuite():
    n = unittest.TestSuite()
    n.addTest(Signup.SignUp("test"))
    n.addTest(General.general())
    n.addTest(Lists.lists())
    n.addTest(Views.views())
    n.addTest(Subtasks.subtasks())
    n.addTest(Files.files())
    return n

driver = webdriver.Firefox()
set_driver(driver)
driver.implicitly_wait(3)
driver.get("http://anydo.github.io/web-client/stable/")

TestRunName = "Web - General Features"
resultLog = InitLog.init_log(TestRunName)
runner = CustomRunner.Runner(stream=resultLog, resultclass=CustomRunner.Result, runName=TestRunName)
runner.run(nsuite())
resultLog.close()
