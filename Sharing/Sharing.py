__author__ = 'Eidan Wasser'
import unittest
import CreateSharedTask, DragBetweenSections, EditSharedTask, Decline, Comment

def sharing():
    n = unittest.TestSuite()

    n.addTest(CreateSharedTask.CreateSharedTask("test"))
    n.addTest(DragBetweenSections.DragBetweenSections("test"))
    n.addTest(EditSharedTask.EditSharedTask("test"))
    n.addTest(Comment.Comment("test"))
    n.addTest(Decline.Decline("test"))

    return n

