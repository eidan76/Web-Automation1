__author__ = 'Eidan Wasser'

import datetime
import os

def init_log(TestRunName):

    d = datetime.datetime.now()
    fileName = d.strftime(format="%y%m%d%H%M%S") + ".txt"
    mainDir = os.getcwd()
    os.chdir(mainDir + "/Results")
    resultLog = open(fileName, "w+")
    os.chdir(mainDir)
    return resultLog