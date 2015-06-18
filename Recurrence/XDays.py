__author__ = 'Eidan Wasser'
import unittest
import time, datetime, random
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from Utils import InitCase, Config, ChangePremium

class XDays(unittest.TestCase):

    def test(self):
        d = datetime.datetime.now()
        X = random.choice(range(1,10))
        Y = random.choice(range(1,4))

        ChangePremium.change_to_premium()
        taskID = InitCase.init_case(menu="ALL", taskOption="open", taskNo=1)
        self.verificationErrors = []

        Config.find_element(Config.task_recurrence).click()
        Config.find_element(Config.recurrenceByType, "DAY").click()

        for t in range(X): Config.find_element(Config.recurrence_everyXPlus).click()
        Config.find_element(Config.recurrence_endsAfter).click()
        for q in range(Y): Config.find_element(Config.recurrence_endsAfterYPlus).click()

        Config.find_element(Config.recurrence_ok).click()
        Config.find_element(Config.task_closeButton).click()

        for h in range(Y):
            d = d + datetime.timedelta(X+1)
            dText = d.strftime("%A %m.%d").replace("0","")

            Config.wait_for_element(Config.task_closeButton, present=False)

            Config.find_element(Config.taskCheckByStatus, "unchecked").click()

            for i in range(20):
                try:
                    if len(Config.find_elements(Config.taskBySectionName, "Upcoming")) == h+1: break
                except: pass
                time.sleep(1)
            else: raise NoSuchElementException

            try: self.assertTrue(Config.is_element_present(Config.taskBySectionName, "Upcoming"))
            except AssertionError as e: self.verificationErrors.append(str(e))

            try: self.assertTrue(Config.find_element(Config.taskRecurringByStatus, "unchecked").is_displayed())
            except AssertionError as e: self.verificationErrors.append(str(e))

            Config.find_element(Config.taskTitleByStatus, "unchecked").click()

            try: self.assertEqual(Config.find_element(Config.task_recurrenceLabel).text, "Every " + str(X+1) + " days, Ends after " + str(Y+1) + " times")
            except AssertionError as e: self.verificationErrors.append(str(e))

            try: Config.find_element(Config.task_TimeSelector).text.index(dText)
            except ValueError as e: self.verificationErrors.append(str(e))

            Config.find_element(Config.task_closeButton).click()

        Config.find_element(Config.taskCheckByStatus, "unchecked").click()
        time.sleep(3)

        try: self.assertEqual(len(Config.find_elements(Config.task)), Y+1)
        except AssertionError as e: self.verificationErrors.append(str(e))

        self.assertEqual([], self.verificationErrors)
