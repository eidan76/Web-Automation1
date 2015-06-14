__author__ = 'Eidan Wasser'

import datetime

def init_log(TestRunName):

    d = datetime.datetime.now()
    fileName = d.strftime(format="%y%m%d%H%M%S") + ".txt"
    resultLog = open(fileName, "w+")

    return resultLog