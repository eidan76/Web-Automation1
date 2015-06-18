__author__ = 'Eidan Wasser'

import unittest

import Add
import Swipe
import Unswipe
import Delete
import Edit


def subtasks():
    n = unittest.TestSuite()
    n.addTest(Add.Add("test"))
    n.addTest(Edit.Edit("test"))
    n.addTest(Swipe.Swipe("test"))
    n.addTest(Unswipe.Unswipe("test"))
    n.addTest(Delete.Delete("test"))
    return n
