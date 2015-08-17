# -*- coding: utf-8 -*-
from selenium.webdriver.common.action_chains import ActionChains
import unittest, time, NewList
from Utils import Config, InitCase

class DragAndDropList(unittest.TestCase):
    
    def test(self):
        InitCase.init_case(menu="MAIN")
        self.verificationErrors = []
        listID = NewList.listID

        list = Config.find_element(Config.main_listByID, listID)
        allTasks = Config.find_element(Config.main_AllTasks)

        #~Drag and Drop~
        ActionChains(Config.get_driver()).click_and_hold(list).perform()
        time.sleep(0.5)
        ActionChains(Config.get_driver()).move_to_element_with_offset(allTasks, 238, 0).perform()
        time.sleep(0.5)
        ActionChains(Config.get_driver()).release().perform()
        time.sleep(1)

        style = list.get_attribute("style")
        left = style.find("left: ") + 6
        position = ""
        for i in range(3):
            position = position + style[left]
            left = left + 1

        try: self.assertEqual("238", position)
        except AssertionError as e: self.verificationErrors.append(str(e))

        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
