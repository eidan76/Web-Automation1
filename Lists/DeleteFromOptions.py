__author__ = 'Eidan Wasser'
# -*- coding: utf-8 -*-
import unittest, time, NewList
from Utils import Config, InitCase

class DeleteFromOptions(unittest.TestCase):

    def test(self, listID = None):
        self.verificationErrors = []
        if listID is None:
            listID = NewList.listID
        InitCase.init_case(menu=listID, taskNo=None)

        Config.find_element(Config.menuButton).click()
        Config.find_element(Config.menu_deleteList).click()
        time.sleep(1)
        Config.find_element(Config.listDeleteConfirm).click()
        time.sleep(2)
        try: self.assertFalse(Config.is_element_present(Config.main_listByID, listID))
        except AssertionError as e: self.verificationErrors.append(str(e))
        self.assertEqual([], self.verificationErrors)

def delete_from_options():
    n = unittest.TestSuite()
    n.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(NewList.NewList))
    n.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(DeleteFromOptions))
    return n

if __name__ == "__main__":
    unittest.main()

