__author__ = 'Eidan Wasser'
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException

import time

def set_driver(param):
    global driver
    driver = param

def get_driver():
    return driver


# this function cam either return an element using a specific task/list ID. If an element ID is given, you must use an array that suites an ID
def find_element(ref, elementID=""):
    if elementID == "":
        return driver.find_element(ref[0], ref[1])
    else:
        return driver.find_element(ref[0], ref[1] + elementID + ref[2])

def find_elements(ref, elementID=""):
    if elementID == "":
        return driver.find_elements(ref[0], ref[1])
    else:
        return driver.find_elements(ref[0], ref[1] + elementID + ref[2])

def is_element_present(ref, elementID=""):
    try:
        if elementID == "":
            driver.find_element(ref[0], ref[1])
        else:
            driver.find_element(ref[0], ref[1] + elementID + ref[2])
    except NoSuchElementException, e: return False
    return True

def wait_for_element(ref, elementID="", present=True, trys=5):
    for i in range(trys):
        try:
            if is_element_present(ref, elementID) == present: break
        except: pass
        time.sleep(1)
    else: raise NoSuchElementException

def wait_for_element_visibility(ref, elementID="", visible=True):
    for i in range(5):
        try:
            if find_element(ref, elementID).is_displayed() == visible: break
        except: pass
        time.sleep(1)
    else: raise ElementNotVisibleException

#References with variables
taskTitleID = [By.XPATH, "(//div[@data-task-id=\"", "\"]//p[@class=\"title\"])"]
taskMarkDoneID = [By.XPATH, "//div[@data-task-id=\"", "\"]//a[@id=\"mark-done\"]"]
taskByID = [By.XPATH, "//div[@data-task-id=\"", "\"]"]
taskBySectionName = [By.XPATH, "//section[@data-category=\"", "\"]//div[@class=\"task-container\" or @class=\"task-container ui-sortable-handle\"]"]
taskTitleBySectionName = [By.XPATH, "//section[@data-category=\"", "\"]//div[@class=\"task-container\" or @class=\"task-container ui-sortable-handle\"]//p"]

list_addTaskToSectionByName = [By.XPATH, "//section[@data-category=\"", "\"]//div[@class=\"add-inline\"]"]
list_sectionByName = [By.XPATH, "//section[@data-category=\"","\"]"]

main_ListNameID = [By.XPATH, "//div[@id=\"", "\"]//div[@class=\"name\"]"]
main_listByName = [By.XPATH, "//div[div=\"","\"]"]
main_listByID = [By.XPATH, "//div[@id=\"", "\"]"]
main_listOptionsID = [By.XPATH, "//div[@id=\"", "\"]/div[@class=\"more\"]"]
main_listDeleteID = [By.XPATH, "//div[@id=\"", "\"]/div[@id=\"overlay\"]/div[@class=\"delete\"]"]
main_listEditID = [By.XPATH, "//div[@id=\"", "\"]/div[@id=\"overlay\"]/div[@class=\"edit\"]"]

task_badgeByIconName = [By.XPATH, "//span[@id=\"", "\"]/span[@data-badge]"]
files_thumbnailByType = [By.XPATH, "//ul[@class=\"file-attachments-list\"]//li//div[@class=\"above-thumbnail type-","\"]"]
fileByName = [By.XPATH, "//ul[@class=\"file-attachments-list\"]//div[\"","\"]"]

#References in expanded tasks
task_editTitle = [By.XPATH, "(//div[@id=\"title-box\"]/textarea[@id=\"title\"])"]
task_closeButton = [By.XPATH, "(//div[@class=\"dialog fbox-center show\"]/div[@class=\"close-button\"])"]
task_FolderSelector = [By.CSS_SELECTOR, "span.folderSelector > span"]
task_ListSelectorItem = [By.XPATH, "//div[@id='folderDialog']//li[@class=\"folder-item\"]"]
task_PrioritySelectorOff = [By.CSS_SELECTOR, "span.prioritySelector"]
task_PrioritySelectorOn = [By.CSS_SELECTOR, "span.prioritySelector.active"]
task_TimeSelector = [By.CSS_SELECTOR, "span.timeSelector > span"]

#Task references in lists
taskCheck = [By.CSS_SELECTOR, "a.check"]
taskTitle = [By.XPATH, "//p[@class=\"title\"]"]
taskMarkDone = [By.CSS_SELECTOR, "a#mark-done"]
taskPriority = [By.CSS_SELECTOR, "div#priority"]
taskCreate_InputBox = [By.CSS_SELECTOR, "textarea#title"]
taskCreate_PlusButton = [By.CSS_SELECTOR, "span#plus-button"]

#Subtask references
subtasks_newTitle = [By.CSS_SELECTOR, "#new-subtask > input[type=\"text\"]"]
subtasks_plusButton = [By.CSS_SELECTOR, "#new-subtask > #plus-button"]
subtasks_title = [By.CSS_SELECTOR, "input.title"]
subtasks_check = [By.CSS_SELECTOR, "a.check"]
subtasks_markDone = [By.CSS_SELECTOR, "a.mark-done"]
subtask = [By.XPATH, "//ul[@class=\"subtasks-list\"]/li"]

#File attachment references
files_addFromComputer = [By.CSS_SELECTOR, "div.file-input-wrapper > input[type=\"file\"]"]
files_progressBar = [By.CSS_SELECTOR, "div.upload.progress-bar"]
files_name = [By.CSS_SELECTOR, "div.content"]
files_delete = [By.CSS_SELECTOR, "img.delete"]
files_deleteConfirm = [By.CSS_SELECTOR, "#no > div.icon"]
files_previewContainer = [By.CSS_SELECTOR, "div.preview-container"]
files_preview = [By.XPATH, "//div[@class=\"preview-container\"]/div"]
files_previewCloseButton = [By.CSS_SELECTOR, "div.close-button.no-tooltip"]
files_previewVideo = [By.XPATH, "//div[@class=\"preview-container\"]/video/source[1]"]
note = [By.CSS_SELECTOR, "textarea#text"]

#References in calender
cal_selectedDay = [By.XPATH, "//div[@class=\"dw-cal-table\"]//div[@aria-selected=\"true\"]"]
cal_dayByDate = [By.XPATH, "//div[@id=\"date\"]//div[@class=\"dw-cal-slide dw-cal-slide-a\"]//div[@data-full=\"", "\"]"]
cal_previousMonth = [By.XPATH, "//div[@class=\"dw-cal-prev-m dw-cal-prev dw-cal-btn dwb dwb-e\"]"]
cal_OK = [By.ID, "ok"]

#Basic references that are not related to specific screens
listTitle = [By.CSS_SELECTOR, "h2#name"]
listTitleEdit = [By.XPATH, "(//div[@id=\"listNameEditDialog\"]//p[@id=\"name\"])"]
goToMainGrid = [By.CSS_SELECTOR, "a#lists"]
openSettings = [By.LINK_TEXT, "Any.do"]
menu = [By.CSS_SELECTOR, "#menu"]
sync = [By.ID, "sync"]
menu_deleteList = [By.CSS_SELECTOR, "div.items > div#delete"]
menu_editList = [By.CSS_SELECTOR, "div.items > div#edit"]
listDeleteConfirm = [By.CSS_SELECTOR, "div#yes > div.icon"]
overlay = [By.CSS_SELECTOR, "div.overlay"]

#Main grid references
main_AllTasks = [By.ID, "pre_all_tasks"]
main_newList = [By.ID, "new"]
main_hayush = [By.ID, "hayush"]

#References in Settings
settings_CompletedTasks = [By.LINK_TEXT, "Completed Tasks"]
completedTask = [By.CSS_SELECTOR, "div.task-content"]
completedTasks_Delete = [By.CSS_SELECTOR, "a.control-button.delete"]
completedTasks_Restore = [By.CSS_SELECTOR, "a.control-button.restore"]
completedTasks_DeleteAll = [By.XPATH, "//div[@id='doneTasks-pane']//div[@class=\"button medium-button light-grey active\"]"]
completedTasks_BackgroundText = [By.XPATH, "//div[@id=\"doneTasks-pane\"]//p[@id=\"title\"]"]

#References in sign-up flow
signUp_emailButton = [By.XPATH, "//a[@class=\"giant-button light-blue signin-email-btn\"]"]
signUp_inputName = [By.ID, "name"]
signUp_inputEmail = [By.ID, "email"]
signUp_inputPass = [By.ID, "password"]
signUp_RegisterButton = [By.XPATH, "//div[@id='button']/div"]
signUp_ErrorMessage = [By.CSS_SELECTOR, "div.error-message"]
#Preset list OK button
signUp_start = [By.ID, "start"]
