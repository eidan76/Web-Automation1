__author__ = 'Eidan Wasser'
import unittest

from Login import Facebook
from Utils import Config

from Login import Signup, Login
from General import General
from Lists import Lists
from Views import Views
from Subtasks import Subtasks
from Files import Files
from Recurrence import Recurrence
from Positioning import Positioning
from DefaultFolder import DefaultFolder
from Sharing import Sharing
from ListSharing import ListSharing
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
    n.addTest(DefaultFolder.default_folder())
    n.addTest(Sharing.sharing())
    n.addTest(ListSharing.list_sharing())
    n.addTest(Login.login())
    return n

driver = Config.init_driver("http://anydo.github.io/web-client/printList/")
Config.set_driver(driver)

TestRunName = "Web - General Features"
# resultLog = InitLog.init_log(TestRunName)
# runner = CustomRunner.Runner(stream=resultLog, resultclass=CustomRunner.Result, runName=TestRunName, base_url=Config.get_base_url())
runner = unittest.TextTestRunner(verbosity=2)
runner.run(nsuite())
# resultLog.close()
