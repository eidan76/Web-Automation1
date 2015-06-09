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

def test_start():
    driver = webdriver.Firefox()
    set_driver(driver)
    driver.implicitly_wait(3)
    driver.get("http://anydo.github.io/web-client/stable/")
    return driver

def nsuite():

    n = unittest.TestSuite()
    n.addTest(Signup.SignUp("test"))
    n.addTest(General.general())
    n.addTest(Lists.lists())
    n.addTest(Views.views())
    n.addTest(Subtasks.subtasks())
    n.addTest(Files.files())

    return n

#if __name__ == "__main__":
driver = test_start()
runner = unittest.TextTestRunner(verbosity=2)
runner.run(nsuite())
