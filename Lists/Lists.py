__author__ = 'Eidan Wasser'

import unittest
from selenium import webdriver
import NewList, EditFromMain, EditFromLongPress, EditFromOptions, DeleteFromMain, DeleteFromOptions, DragAndDropList

def lists():
    n = unittest.TestSuite()
    n.addTest(NewList.NewList("test"))
    #n.addTest(DragAndDropList.DragAndDropList("test"))
    n.addTest(EditFromMain.EditMain("test"))
    #n.addTest(EditFromLongPress.EditFromLongPress("test"))
    #n.addTest(EditFromOptions.EditFromOptions("test"))
    #n.addTest(DeleteFromMain.DeleteMain("test"))
    #n.addTest(DeleteFromOptions.delete_from_options())

    return n
