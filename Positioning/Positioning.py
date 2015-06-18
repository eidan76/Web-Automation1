__author__ = 'Eidan Wasser'
import unittest
import ListView
import ListViewALL
import PriorityView
import DateView

def positioning():
    n = unittest.TestSuite()

    n.addTest(ListView.ListView("test"))
    n.addTest(ListViewALL.ListViewALL("test"))
    n.addTest(PriorityView.PriorityView("test"))
    n.addTest(DateView.DateView("test"))

    return n