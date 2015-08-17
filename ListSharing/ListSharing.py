__author__ = 'Eidan Wasser'
import unittest
import CreateSharedList, AddTaskToSharedList, ChangeFromSharedList, ChangeToSharedList, CompleteTask

def list_sharing():
    n = unittest.TestSuite()

    n.addTest(CreateSharedList.CreateSharedList("test"))
    n.addTest(AddTaskToSharedList.AddTaskToSharedList("test"))
    n.addTest(ChangeFromSharedList.ChangeFromSharedList("test"))
    n.addTest(ChangeToSharedList.ChangeToSharedList("test"))
    n.addTest(CompleteTask.CompleteTask("test"))
    return n

