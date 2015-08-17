__author__ = 'Eidan Wasser'
import unittest
import ChangeDefaultFolder

def default_folder():
    n = unittest.TestSuite()

    n.addTest(ChangeDefaultFolder.ChangeDefaultFolder("test"))
    return n