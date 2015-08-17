__author__ = 'Eidan Wasser'
from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException

def delete_accounts():

    driver = webdriver.Firefox()
    userlist = ["1436345204.76@any.do",
"1436357875.18@any.do",
"1436357991.75@any.do",
"1436358152.26@any.do",
"1436358472.09@any.do",
"1436358633.11@any.do",
"1436358790.88@any.do",
"1436359082.74@any.do",
"1436359281.17@any.do",
"1436359629.83@any.do",
"1436360008.72@any.do",
"1436360168.54@any.do",
"1436360955.27@any.do",
"1436361388.71@any.do",
"1436428067.59@any.do",
"1436428408.73@any.do",
"1436429015.36@any.do",
"1436430053.53@any.do",
"1436430134.34@any.do",
"1436430147.15@any.do",
"1436430838.78@any.do",
"1436430850.62@any.do",
"1436431218.79@any.do",
"1436431795.87@any.do",
"1436431815.8@any.do",
"1436431886.89@any.do",
"1436431914.33@any.do",
"1436432190.53@any.do",
"1436432219.89@any.do",
"1436432232.24@any.do",
"1436432271.75@any.do",
"1436432293.08@any.do",
"1436432499.12@any.do",
"1436432522.9@any.do"]

    driver.get("http://anydo-support-portal.herokuapp.com/")

    for x in userlist:
        driver.find_element_by_css_selector("input#deleteEmail").send_keys(x)
        driver.find_element_by_xpath("//input[@value=\"Delete User\"]").click()
        for i in range(3):
            try:
                if driver.find_element_by_css_selector("div#message").text == "User " + x + " was successfully deleted":
                    break
            except: pass
            time.sleep(1)
        else:
            driver.get("http://anydo-support-portal.herokuapp.com/")
            print "Error deleting user " + x
            continue
        print x + " deleted"

delete_accounts()