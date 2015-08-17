__author__ = 'Eidan Wasser'
import unittest
import Daily
import Weekly
import Monthly
import Yearly
import DragToSomeday
import SomedayToRecurring
import WeeklyPremium
import MonthlyPremium
import XDays

def recurrence():
    n = unittest.TestSuite()

    n.addTest(Daily.Daily("test"))
    n.addTest(Weekly.Weekly("test"))
    n.addTest(Monthly.Monthly("test"))
    n.addTest(Yearly.Yearly("test"))
    n.addTest(DragToSomeday.DragSomeday("test"))
    n.addTest(SomedayToRecurring.SomedayToRecurring("test"))
    n.addTest(WeeklyPremium.WeeklyPremium("test"))
    n.addTest(MonthlyPremium.MonthlyPremium("test"))
    n.addTest(XDays.XDays("test"))
    return n

