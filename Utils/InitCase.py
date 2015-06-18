__author__ = 'Eidan Wasser'

import time
import Config, ClearAllTasks, CreateTaskF
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

def init_case(menu="", view="", taskOption="", taskNo = 1):
    taskIDs = None

    #makes sure there is no overlay like when you enter the notification area or settings
    if Config.find_element(Config.overlay).is_displayed() == True:
        Config.find_element(Config.overlay).click()
    if Config.is_element_present(Config.confirmDialog) == True:
        Config.find_element(Config.confirmDialog_cancel).click()

    if menu != "": taskIDs = select_menu(menu, taskNo, view)
    if view != "": select_view(view)
    if taskOption != "": task_options(taskOption)
    else: close_task()
    return taskIDs

def task_options(taskOption):

    #If you want to keep a task expanded, specify a page to open: "note", "subtasks", "files", "share".
    # To automatically collapse the task, leave empty
    if Config.is_element_present(Config.task_editTitle) == False:
        Config.find_element(Config.taskTitle).click()
    if taskOption == "open":
      pass
    elif Config.find_element([By.CSS_SELECTOR, "span#" + taskOption]).get_attribute("class") != "tab-header selected":
        Config.find_element([By.CSS_SELECTOR, "span#" + taskOption]).click()

def close_task():

    if Config.is_element_present(Config.task_closeButton):
            try: Config.find_element(Config.task_closeButton).click()
            except NoSuchElementException: pass

def select_menu(menu, taskNo, view):

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
        return add_tasks_as_needed(taskNo, view)

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
        return add_tasks_as_needed(taskNo, view)

def select_view(view):

    #Selects a view inside a list
    if view != "":
        if Config.find_element([By.CSS_SELECTOR, "a#" + view]).get_attribute("class") != "view topbar-icon selected":
            Config.find_element([By.CSS_SELECTOR, "a#" + view]).click()

def add_tasks_as_needed(taskNo, view):

    tasks = Config.find_elements(Config.task)
    activeTasks = Config.find_elements(Config.taskTitleByStatus, "unchecked")
    taskIDs = []
    if len(tasks) == taskNo == len(activeTasks):
        for t in tasks:
            taskIDs.append(t.get_attribute("data-task-id"))
    else:
        if tasks != []:
            ClearAllTasks.clear_all_tasks()
        for i in range(taskNo):
            taskID = CreateTaskF.create_a_task(i)
            taskIDs.append(taskID)

    if len(taskIDs) == 1: return taskIDs[0]
    else: return taskIDs

