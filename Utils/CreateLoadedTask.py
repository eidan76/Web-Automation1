__author__ = 'Eidan Wasser'
import Config
import InitCase

def create_loaded_task():

    InitCase.task_options(taskOption="subtasks")
    Config.find_element(Config.subtasks_newTitle).clear()
    Config.find_element(Config.subtasks_newTitle).send_keys("subtask")
    Config.find_element(Config.subtasks_plusButton).click()

    InitCase.task_options("note")
    noteText = "test test test test test test test test test test test test test test test test test test test test test test "
    Config.find_element(Config.note).send_keys(noteText)

    InitCase.task_options("files")
    Config.find_element(Config.files_addFromComputer).send_keys("C:\\Users\\Eidan Wasser\\PycharmProjects\\Suite1\\Files\\2015-03-29.png")
    Config.wait_for_element(Config.files_progressBar, present=False)

    InitCase.task_options("open")
    Config.wait_for_element(Config.task_PrioritySelector)
    Config.find_element(Config.task_PrioritySelector).click()
