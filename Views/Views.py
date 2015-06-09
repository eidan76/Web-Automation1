__author__ = 'Eidan Wasser'

import unittest

import PriorityHighDrag
import DateTomorrowDrag
import DateUpcoming
import DateSomedayDrag
import PriorityNormalDrag
import PriorityHighView
import PriorityNormalView
import PriorityHighAdd
import DateTodayAdd
from Utils import InitSuite


def views():
    n = unittest.TestSuite()

    n.addTest(InitSuite.InitSuite("test"))
    n.addTest(PriorityHighDrag.PriorityHighDrag("test"))
    n.addTest(PriorityNormalDrag.PriorityNormalDrag("test"))
    n.addTest(PriorityHighView.PriorityHighView("test"))
    n.addTest(PriorityNormalView.PriorityNormalView("test"))
    n.addTest(PriorityHighAdd.PriorityHighAdd("test"))
    n.addTest(InitSuite.InitSuite("test"))
    n.addTest(DateTomorrowDrag.DragTomorrow("test"))
    n.addTest(DateUpcoming.Upcoming("test"))
    n.addTest(DateSomedayDrag.DragSomeday("test"))
    n.addTest(DateTodayAdd.TodayAdd("test"))

    return n
