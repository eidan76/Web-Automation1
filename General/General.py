__author__ = 'Eidan Wasser'
import unittest

import CreateTask
import EditTitle
import ChangeList
import Swipe
import Unswipe
import Delete
import RestoreFromDoneList
import DeleteFromDoneList
import DeleteFromDoneListAll
import PriorityHigh
import PriorityNormal

def general():

    n = unittest.TestSuite()
    n.addTest(CreateTask.CreateATask("test"))
    n.addTest(EditTitle.EditTitle("test"))
    n.addTest(PriorityHigh.PriorityHigh("test"))
    n.addTest(PriorityNormal.PriorityNormal("test"))
    n.addTest(ChangeList.ChangeList("test"))
    n.addTest(Swipe.Swipe("test"))
    n.addTest(Unswipe.Unswipe("test"))
    n.addTest(Delete.Delete("test"))
    n.addTest(RestoreFromDoneList.RestoreFromDeleted("test"))
    n.addTest(DeleteFromDoneList.DeleteFromDoneListOne("test"))
    n.addTest(DeleteFromDoneListAll.DeleteFormDoneListAll("test"))

    return n
