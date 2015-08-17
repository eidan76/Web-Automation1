__author__ = 'Eidan Wasser'
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium import webdriver
import time

def init_driver(base_url):
    driver = webdriver.Firefox()
    driver.implicitly_wait(2)
    set_base_url(base_url)
    driver.get(get_base_url())
    return driver

def set_driver(param):
    global driver
    driver = param

def get_driver():
    return driver

def set_base_url(param):
    global base_url
    base_url = param

def get_base_url():
    return base_url

def sync():
    find_element(menuButton).click()
    for i in range(3):
        if not is_element_present(menu):
            find_element(menuButton).click()
        else: break
    find_element(syncButton).click()
    try: wait_for_element(syncButton, present=False, trys=30)
    except NoSuchElementException: raise SyncFailure

class SyncFailure(Exception):
    def __str__(self):
        return "Sync timed out after 30 seconds"


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

def wait_for_element(ref, elementID="", present=True, trys=20):
    for i in range(trys):
        try:
            if is_element_present(ref, elementID) == present: break
        except: pass
        time.sleep(1)
    else: raise NoSuchElementException

def wait_for_element_visibility(ref, elementID="", visible=True, trys=20):
    for i in range(trys):
        try:
            if find_element(ref, elementID).is_displayed() == visible: break
        except: pass
        time.sleep(1)
    else: raise ElementNotVisibleException

#References with variables
taskTitleID = [By.CSS_SELECTOR, "div[data-task-id=\"", "\"] p.title"] #C
taskCheckID = [By.CSS_SELECTOR, "div[data-task-id=\"", "\"] a.check"] #C
taskCheckByStatus = [By.CSS_SELECTOR, "div.task-container[data-status=\"","\"] a.check"] #C
taskMarkDoneID = [By.XPATH, "//div[@data-task-id=\"", "\"]//a[@id=\"mark-done\"]"]
taskByID = [By.XPATH, "//div[@data-task-id=\"", "\"]"]
taskBySectionName = [By.CSS_SELECTOR, "section[data-category=\"", "\"] div.task-container"] #C
taskTitleBySectionName = [By.CSS_SELECTOR, "section[data-category=\"", "\"] div.task-container p"] #C
taskTitleByStatus = [By.CSS_SELECTOR, "div.task-container[data-status=\"","\"] p"] #C
taskRecurringByID = [By.XPATH, "//div[@data-task-id=\"", "\"]//a[@id=\"recurring\"]"]
taskRecurringByStatus = [By.XPATH, "//div[@data-status=\"", "\"]//a[@id=\"recurring\"]"]

list_addTaskToSectionByName = [By.CSS_SELECTOR, "section[data-category=\"", "\"] div.add-inline"] #C
list_sectionByName = [By.XPATH, "//section[@data-category=\"","\"]"]

task_badgeByIconName = [By.XPATH, "//span[@id=\"", "\"]/span[@data-badge]"]
files_thumbnailByType = [By.CSS_SELECTOR, "li.file-attachment-item div.mime-thumbnail.type-","]"]#C
fileByName = [By.XPATH, "//ul[@class=\"file-attachments-list\"]//div[\"","\"]"] #OK
recurrenceByType = [By.XPATH, "//ul[@id=\"repeatMethod\"]/li[@data-id=\"TASK_REPEAT_","\"]"]
recurrence_weekdayByName = [By.XPATH, "//div[@id=\"repeatDays\"]//span[@data-id=\"","\"]"]

#References in expanded tasks
task_editTitle = [By.XPATH, "(//div[@id=\"title-box\"]/div[@id=\"title\"])"]
task_closeButton = [By.CSS_SELECTOR, "div.dialog.fbox-center.show > div.close-button"]
task_FolderSelector = [By.CSS_SELECTOR, "span.folderSelector > span"]
task_ListSelectorItem = [By.CSS_SELECTOR, "div#folderDialog li.folder-item"] #C
task_ListSelectorItemByID = [By.XPATH, "//div[@id=\"folderDialog\"]//li[@data-id=\"","\"]"]
task_PrioritySelector = [By.CSS_SELECTOR, "span.prioritySelector"]
task_TimeSelector = [By.CSS_SELECTOR, "span.timeSelector > span"]
task_recurrence = [By.CSS_SELECTOR, "span.recurring-icon"]
task_recurrenceLabel = [By.CSS_SELECTOR, "span.recurringSelector span.label"] #C

#Task references in lists
task = [By.CSS_SELECTOR, "div.task-container"] #C
taskCheck = [By.CSS_SELECTOR, "div[data-status=\"unchecked\"] a.check"] #C
taskTitle = [By.CSS_SELECTOR, "p.title"] #C
taskMarkDone = [By.XPATH, "//div[@data-status=\"checked\"]//a[@id=\"mark-done\"]"]
taskPriority = [By.CSS_SELECTOR, "div#priority"]
taskRecurring = [By.CSS_SELECTOR, "a#recurring"]
taskSharedAssignee = [By.CSS_SELECTOR, "a#share.assignee"]
taskShare = [By.CSS_SELECTOR, "a#share"]
taskCreate_InputBox = [By.CSS_SELECTOR, "div#title"]
taskCreate_PlusButton = [By.CSS_SELECTOR, "div#task.add span#plus-button"]

#Subtask references
subtasks_newTitle = [By.CSS_SELECTOR, "#new-subtask > input[type=\"text\"]"]
subtasks_plusButton = [By.CSS_SELECTOR, "#new-subtask > #plus-button"]
subtasks_title = [By.CSS_SELECTOR, "ul.subtasks-list div.title"]
subtasks_check = [By.CSS_SELECTOR, "ul.subtasks-list a.check"]
subtasks_markDone = [By.CSS_SELECTOR, "ul.subtasks-list a.mark-done"]
subtask = [By.CSS_SELECTOR, "ul.subtasks-list > li"] #C

#File attachment references
files_addFromComputer = [By.CSS_SELECTOR, "div.file-input-wrapper > input[type=\"file\"]"]
files_progressBar = [By.CSS_SELECTOR, "div.upload.progress-bar"]
files_name = [By.CSS_SELECTOR, "div.content"]
files_delete = [By.CSS_SELECTOR, "li.file-attachment-item div.delete"]
files_deleteConfirm = [By.CSS_SELECTOR, "#no > div.icon"]
files_previewContainer = [By.CSS_SELECTOR, "div.preview-container"]
files_preview = [By.CSS_SELECTOR, "div.preview-container > div"] #C
files_previewCloseButton = [By.CSS_SELECTOR, "div.close-button.no-tooltip"]
files_previewVideo = [By.CSS_SELECTOR, "div.preview-container > video > source"] #C
note = [By.CSS_SELECTOR, "div#text"]
files_dropbox = [By.CSS_SELECTOR, "div.dropbox-file-input-wrapper"] #C
files_google = [By.CSS_SELECTOR, "div.drive-file-input-wrapper"]
driveFrame = [By.CSS_SELECTOR, "iframe.picker-frame.picker-dialog-frame"]

recurrence_ok = [By.ID, "ok"]
recurrence_selectedDays = [By.CSS_SELECTOR, "span.day.selected"]
recurrence_monthlyDayOfWeek = [By.CSS_SELECTOR, "li#week.monthType"]
recurrence_everyXPlus = [By.CSS_SELECTOR, "div.counter > div.controls > div.plus"]
recurrence_endsAfter = [By.CSS_SELECTOR, "li#REPEAT_END_OCCURRENCES"]
recurrence_endsAfterYPlus = [By.CSS_SELECTOR, "li#REPEAT_END_OCCURRENCES div.plus"] #C

sharing_inputEmail = [By.XPATH, "//div[@id=\"add-invitee\"]/input[@id=\"email\"]"]
sharing_commitEmailButton = [By.CSS_SELECTOR, "span#commit-invitee-button"]
sharing_sendInvites = [By.CSS_SELECTOR, "span#send-invites-button.active"]
sharing_inviteOverlay = [By.CSS_SELECTOR, "div#invite-overlay.open"]
sharing_memberBadgeByEmail = [By.CSS_SELECTOR, "span.person[data-target=\"","\"]"] #C
sharing_memberPopup = [By.CSS_SELECTOR, "div.member-popup"] #C
sharing_badgeStatus = [By.CSS_SELECTOR, "div.member-popup div.member > div:nth-last-child(1)"] #C
sharing_badgeEmail = [By.CSS_SELECTOR, "div.member-popup div.name.one-line-text"] #C
sharing_commentInput = [By.CSS_SELECTOR, "input#comment-text"]
sharing_addCommentButton = [By.CSS_SELECTOR, "a#add-comment-button"]
sharing_commentAuthor = [By.CSS_SELECTOR, "ul#comments-list > li:nth-last-child(1) span.author"] #C
sharing_commentText = [By.CSS_SELECTOR, "ul#comments-list > li:nth-last-child(1) span.enable-selection"] #C

#References in calender
cal_selectedDay = [By.XPATH, "//div[@class=\"dw-cal-table\"]//div[@aria-selected=\"true\"]"] #OK
cal_dayByDate = [By.XPATH, "//div[@id=\"date\"]//div[@class=\"dw-cal-slide dw-cal-slide-a\"]//div[@data-full=\"", "\"]"] #OK
cal_previousMonth = [By.XPATH, "//div[@class=\"dw-cal-prev-m dw-cal-prev dw-cal-btn dwb dwb-e\"]"] #OK
cal_OK = [By.ID, "ok"]

#Basic references that are not related to specific screens
listTitle = [By.CSS_SELECTOR, "h2#name"]
listTitleEdit = [By.XPATH, "//div[@id=\"listNameEditDialog\"]//p[@id=\"name\"]"]
goToMainGrid = [By.CSS_SELECTOR, "a#lists"]
openSettings = [By.LINK_TEXT, "Any.do"]
menuButton = [By.CSS_SELECTOR, "a.topbar-icon div#menu"]
menu = [By.CSS_SELECTOR, "div.menu-popup.show"]
syncButton = [By.ID, "sync"]
menu_deleteList = [By.CSS_SELECTOR, "div.items > div#delete"]
menu_editList = [By.CSS_SELECTOR, "div.items > div#edit"]
listDeleteConfirm = [By.CSS_SELECTOR, "div#yes > div.icon"]
list_addTask = [By.CSS_SELECTOR, "div.add-inline"]
list_addSharedMemberButton = [By.CSS_SELECTOR, "span#toggle-invite-overlay-button"]
list_sharedMemberByEmail = [By.XPATH, "//div[@id=\"list-header\"]//span[@id=\"people\"]//span[@data-target=\"","\"]"] #C
overlay = [By.CSS_SELECTOR, "div.overlay"]
confirmDialog = [By.ID, "confirmDialog"]
confirmDialog_cancel = [By.XPATH, "//div[@id=\"confirmDialog\"]//div[@id=\"cancel\"]//div"]
confirmDialog_OK = [By.XPATH, "//div[@id=\"confirmDialog\"]//div[@id=\"yes\"]//div"]
sharingInvitation = [By.CSS_SELECTOR, "div.invite-popup.show"] #C
sharingInvitation_title = [By.CSS_SELECTOR, "div.invite-popup.show span.bar"]#C
sharingInvitation_accept = [By.CSS_SELECTOR, "div#accept"]
sharingInvitation_decline = [By.CSS_SELECTOR, "div#reject"]
profilePic = [By.CSS_SELECTOR, "a#avatar"]
list = [By.CSS_SELECTOR, "div#listFullView"]

#Main grid references
main_AllTasks = [By.ID, "pre_all_tasks"]
main_newList = [By.ID, "new"]
main_hayush = [By.ID, "hayush"]
main_ListNameID = [By.CSS_SELECTOR, "div[id=\"", "\"] > div.name"] #C
main_listByName = [By.XPATH, "//div[div=\"","\"]"]
main_listByID = [By.XPATH, "//div[@id=\"", "\"]"]
main_listOptionsID = [By.CSS_SELECTOR, "div[id=\"", "\"] > div.more"] #C
main_listDeleteID = [By.CSS_SELECTOR, "div[id=\"", "\"] > div#overlay > div.delete"] #C
main_listEditID = [By.CSS_SELECTOR, "div[id=\"", "\"] > div#overlay > div.edit"] #C
main_list = [By.XPATH, "//div[@id=\"lists\"]/div"]
main_sharedListMembersByListID = [By.XPATH, "//div[@id=\"", "\"]//span[@id=\"people\"]/span"]

#References in Settings
settings_CompletedTasks = [By.LINK_TEXT, "Completed Tasks"]
completedTask = [By.CSS_SELECTOR, "div.task-content"]
completedTasks_Delete = [By.CSS_SELECTOR, "a.control-button.delete"]
completedTasks_Restore = [By.CSS_SELECTOR, "a.control-button.restore"]
completedTasks_DeleteAll = [By.CSS_SELECTOR, "div#doneTasks-pane div.delete-all div.button"] #C
completedTasks_BackgroundText = [By.XPATH, "//div[@id=\"doneTasks-pane\"]//p[@id=\"title\"]"]
settings_accountStatus = [By.CSS_SELECTOR, "p#profile-title > span"]
settings_profile = [By.CSS_SELECTOR, "li#profile"]
settings_email = [By.CSS_SELECTOR, "p.userDetails"]
settings_preferences = [By.CSS_SELECTOR, "li#prefrences"]
preferences_defaultList = [By.CSS_SELECTOR, "li#default"]
defaultList_changeDefault = [By.CSS_SELECTOR, "div#default-pane li:not(.selected)"] #C
profile_signOut = [By.CSS_SELECTOR, "li#sign-out"]
settingsPane = [By.CSS_SELECTOR, "div#settings-pane.open-pane"]

#References in sign-up flow
signUp_emailButton = [By.CSS_SELECTOR, "a.signin-email-btn"] #C
signUp_inputName = [By.ID, "name"]
signUp_inputEmail = [By.ID, "email"]
signUp_inputPass = [By.ID, "password"]
signUp_RegisterButton = [By.XPATH, "//div[@id='button']/div"]
signUp_ErrorMessage = [By.CSS_SELECTOR, "div.error-message"]
#Preset list OK button
signUp_start = [By.ID, "start"]
signIn_button = [By.CSS_SELECTOR, "button.button.giant-button.light-blue.signin"]
signIn_alreadyMember = [By.CSS_SELECTOR, "a.join"]
signIn_inputEmail = [By.CSS_SELECTOR, "form#emailSignin > input#email"]
signIn_inputPass = [By.CSS_SELECTOR, "form#emailSignin > input#password"]
signIn_googlePlus = [By.CSS_SELECTOR, "div.small-social-button.signin-google-btn"]
signIn_facebook = [By.CSS_SELECTOR, "div.small-social-button.signin-facebook-btn"]
singUp_GooglePlusButton = [By.CSS_SELECTOR, "a.giant-button.signin-google-btn"]
singUp_FacebookButton = [By.CSS_SELECTOR, "a.giant-button.signin-facebook-btn"]
signUp_skipWhatsNew = [By.CSS_SELECTOR, "div#skip.textButton"]

def set_sender(param):
    global sender
    sender = param

def get_sender():
    return sender

def set_receiver(param):
    global receiver
    receiver = param

def get_receiver():
    return receiver
