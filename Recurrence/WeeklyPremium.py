__author__ = 'Eidan Wasser'
import unittest
import time, datetime, random
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from Utils import InitCase, Config, ChangeUser


class WeeklyPremium(unittest.TestCase):

    def test(self):
        d = datetime.datetime.now()
        wx = d.strftime("%a").upper()
        days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
        selectedDays = []
        for i in range(3):
            x = random.choice(days)
            selectedDays.append(x)
            days.remove(x)

        ChangeUser.change_to_premium()
        taskID = InitCase.init_case(menu="ALL", taskOption="open", taskNo=1)
        self.verificationErrors = []

        Config.find_element(Config.task_recurrence).click()
        Config.find_element(Config.recurrenceByType, "WEEK").click()

        for day in selectedDays:
            Config.find_element(Config.recurrence_weekdayByName, day).click()

        selectedRep = []
        for sel in Config.find_elements(Config.recurrence_selectedDays):
            selectedRep.append(sel.get_attribute("data-id"))

        Config.find_element(Config.recurrence_ok).click()
        Config.find_element(Config.task_closeButton).click()

        for p in range(len(selectedRep)):
            wday = selectedRep[p]

            Config.wait_for_element(Config.task_closeButton, present=False)

            Config.find_element(Config.taskCheckByStatus, "unchecked").click()

            for i in range(20):
                try:
                    if len(Config.find_elements(Config.taskBySectionName, "Upcoming\" or @data-category=\"Tomorrow")) == p+1: break
                except: pass
                time.sleep(1)
            else: raise NoSuchElementException

            try: self.assertTrue(Config.is_element_present(Config.taskBySectionName, "Upcoming\" or @data-category=\"Tomorrow"))
            except AssertionError as e: self.verificationErrors.append(str(e))

            try: self.assertTrue(Config.find_element(Config.taskRecurringByStatus, "unchecked").is_displayed())
            except AssertionError as e: self.verificationErrors.append(str(e))

            Config.find_element(Config.taskTitleByStatus, "unchecked").click()

            try: Config.find_element(Config.task_recurrenceLabel).text.index(wday.capitalize())
            except ValueError as e: self.verificationErrors.append(str(e))

            try: Config.find_element(Config.task_TimeSelector).text.index(self.next_weekday(selectedRep, p))
            except ValueError as e: self.verificationErrors.append(str(e))

            Config.find_element(Config.task_closeButton).click()

        self.assertEqual([], self.verificationErrors)

    def next_weekday(self, selectedRep, iter):
        d = datetime.datetime.now()
        dayDict = {"SUN":0, "MON":1, "TUE":2, "WED":3, "THU":4, "FRI":5, "SAT":6}
        daydelta = []
        for k in selectedRep:
            s = dayDict[k] - int(d.strftime("%w"))
            if s <= 0: s += 7
            daydelta.append(s)
        for j in range(iter):
           daydelta.remove(min(daydelta))
        l = min(daydelta)
        if l == 1: return "Tomorrow"
        ld = d + datetime.timedelta(l)
        w = ld.strftime("%A %m.%d")
        n=""
        for i in range(len(w)):
            if w[i] != "0":
                n = n + w[i]
        return n