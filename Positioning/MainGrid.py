# -*- coding: utf-8 -*-
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import unittest, time, random
from Utils import Config, InitCase

class MainGrid(unittest.TestCase):
    
    def test(self):
        driver = Config.get_driver()
        InitCase.init_case(menu="MAIN")
        self.verificationErrors = []

        lists = Config.find_elements(Config.main_list)
        for l in lists:
            if l.get_attribute("id") in ["pre_all_tasks", "new"]: lists.remove(l)
        listsToAdd = range(4-len(lists))
        for lst in listsToAdd:
            Config.find_element(Config.main_newList).click()
            Config.find_element(Config.listTitleEdit).send_keys(str(lst))
            Config.find_element(Config.listTitleEdit).send_keys(Keys.ENTER)
            lists.append(Config.find_element(Config.main_listByName, str(lst)))

        allTasks = Config.find_element(Config.main_AllTasks)

        for i in range(3):
            ActionChains(Config.get_driver()).click_and_hold(random.choice(lists)).perform()
            time.sleep(0.5)
            ActionChains(Config.get_driver()).move_to_element_with_offset(allTasks, 238, 0).perform()
            time.sleep(0.5)
            ActionChains(Config.get_driver()).release().perform()
            time.sleep(1)

        listPositions = {}
        for li in lists:
            listPositions[li.get_attribute("id")] = self.get_position(li)

        mainWindow = driver.current_window_handle
        driver.execute_script("$(window.open())")
        window2 = driver.window_handles
        window2.remove(mainWindow)
        driver.switch_to_window(window2)
        driver.get(Config.get_base_url())

        InitCase.init_case(menu="MAIN")
        window2Lists = Config.find_elements(Config.main_list)
        for ls in window2Lists:
            if ls.get_attribute("id") in ["pre_all_tasks", "new"]: window2Lists.remove(ls)

        for lt in window2Lists:
            try: self.assertEqual(self.get_position(lt), listPositions[lt.get_attribute("id")])
            except AssertionError as e: self.verificationErrors.append(e)
        driver.close()
        driver.switch_to_window(mainWindow)

        self.assertEqual([], self.verificationErrors)

    def get_position(self, folder):
        style = folder.get_attribute("style")
        left = style.find("left: ") + 6
        position = ""
        for i in range(3):
            position = position + style[left]
            left = left + 1
        return position

if __name__ == "__main__":
    unittest.main()
