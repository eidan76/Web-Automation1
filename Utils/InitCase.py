__author__ = 'Eidan Wasser'

import time
import Config, ClearAllTasks, CreateTaskF
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.common.by import By

def init_case(menu="", view="", taskOption="", taskNo = 1):
    taskIDs = None

    # a series of actions to ensure you are not starting the test with an unwanted lightbox
    counter=0
    while Config.find_element(Config.overlay).is_displayed():
        try: Config.find_element(Config.overlay).click()
        except ElementNotVisibleException: break
        counter+=1
        if counter >= 3: raise ElementNotClickableException
    if Config.is_element_present(Config.confirmDialog) == True:
        try: Config.find_element(Config.confirmDialog_cancel).click()
        except NoSuchElementException: pass
    if taskOption == "": close_task()



    # Sends you to the screen you want to be in for any test
    if menu != "": select_menu(menu)
    if menu != "MAIN" and taskNo is not None: taskIDs = add_tasks_as_needed(taskNo)
    if view != "": select_view(view)
    if taskOption != "": task_options(taskOption)
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
    counter = 0
    while Config.is_element_present(Config.task_closeButton):
        try: Config.find_element(Config.task_closeButton).click()
        except ElementNotClickableException: break
        counter+=1
        if counter >=3: break

def select_menu(menu):

    #Selects a menu for you to be in, "ALL" / "MAIN" / or list ID to enter a specific list
    if menu == "ALL":
        if Config.is_element_present(Config.list):
            if Config.find_element(Config.listTitle).text != "ALL":
                close_task()
                Config.find_element(Config.goToMainGrid).click()
                time.sleep(2)
                Config.find_element(Config.main_AllTasks).click()
        else: Config.find_element(Config.main_AllTasks).click()

    elif menu == "MAIN":
        close_task()
        try: Config.find_element(Config.goToMainGrid).click()
        except NoSuchElementException: pass

    else:
        if Config.is_element_present(Config.list):
            if Config.find_element(Config.main_ListNameID, menu).text != Config.find_element(Config.listTitle).text:
                close_task()
                Config.find_element(Config.goToMainGrid).click()
                time.sleep(2)
                Config.find_element(Config.main_ListNameID, menu).click()
        else: Config.find_element(Config.main_ListNameID, menu).click()

def select_view(view):

    #Selects a view inside a list
    if view != "":
        if Config.find_element([By.CSS_SELECTOR, "a#" + view]).get_attribute("class") != "view topbar-icon selected":
            close_task()
            Config.find_element([By.CSS_SELECTOR, "a#" + view]).click()

def add_tasks_as_needed(taskNo):

    tasks = Config.find_elements(Config.task)
    activeTasks = Config.find_elements(Config.taskTitleByStatus, "unchecked")
    taskIDs = []
    if len(tasks) == taskNo == len(activeTasks):
        for t in tasks:
            taskIDs.append(t.get_attribute("data-task-id"))
    else:
        close_task()
        if tasks != []:
            ClearAllTasks.clear_all_tasks()
        for i in range(taskNo):
            taskID = CreateTaskF.create_a_task(i)
            taskIDs.append(taskID)

    if len(taskIDs) == 1: return taskIDs[0]
    else: return taskIDs

class ElementNotClickableException(Exception):
    def __str__(self):
        return "Cannot click element"