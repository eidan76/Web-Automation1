__author__ = 'Eidan Wasser'

import time
import Config
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

def init_case(menu="", view="", taskOption=""):

    #makes sure there is no overlay like when you enter the notification area or settings
    if Config.find_element(Config.overlay).is_displayed() == True:
        Config.find_element(Config.overlay).click()

    if menu != "": select_menu(menu)
    if view != "": select_view(view)
    if taskOption != "": task_options(taskOption)
    else: close_task()

def task_options(taskOption):

    #If you want to keep a task expanded, specify a page to open: "note", "subtasks", "files", "share".
    # To automatically collapse the task, leave empty
    if Config.is_element_present(Config.task_editTitle) == False:
        Config.find_element(Config.taskTitle).click()
    if Config.find_element([By.CSS_SELECTOR, "span#" + taskOption]).get_attribute("class") != "tab-header selected":
        Config.find_element([By.CSS_SELECTOR, "span#" + taskOption]).click()

def close_task():

    if Config.is_element_present(Config.task_closeButton):
            try: Config.find_element(Config.task_closeButton).click()
            except NoSuchElementException: pass

def select_menu(menu):

    #Selects a menu for you to be in, "ALL" / "MAIN" / or list ID to enter a specific list
    if menu == "ALL":
        try:
            if Config.find_element(Config.listTitle).text != "ALL":
                close_task()
                Config.find_element(Config.goToMainGrid).click()
                time.sleep(2)
                Config.find_element(Config.main_AllTasks).click()
        except NoSuchElementException:
            Config.find_element(Config.main_AllTasks).click()

    elif menu == "MAIN":
        close_task()
        try: Config.find_element(Config.goToMainGrid).click()
        except NoSuchElementException: pass

    else:
        try:
            if Config.find_element(Config.main_ListNameID, menu).text != Config.find_element(Config.listTitle).text:
                close_task()
                Config.find_element(Config.listTitle).click()
                Config.find_element(Config.main_AllTasks).click()
        except NoSuchElementException:
            Config.find_element(Config.main_ListNameID, menu).click()


def select_view(view):

    #Selects a view inside a list
    if view != "":
        if Config.find_element([By.CSS_SELECTOR, "a#" + view]).get_attribute("class") != "view topbar-icon selected":
            Config.find_element([By.CSS_SELECTOR, "a#" + view]).click()

