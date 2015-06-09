__author__ = 'Eidan Wasser'
from selenium import webdriver
import time

def delete_accounts():

    driver = webdriver.Firefox()
    driver.get("http://anydo-support-portal.herokuapp.com/")
    userlist = []

    for x in userlist:
        driver.find_element_by_css_selector("input#deleteEmail").send_keys(x)
        driver.find_element_by_xpath("//input[@value=\"Delete User\"]").click()
        for i in range(3):
            try:
                if driver.find_element_by_css_selector("div#message").text == "User " + x + " was successfully deleted":
                    break
            except: pass
            time.sleep(1)
        else: "time out"
        print x + " deleted"

delete_accounts()