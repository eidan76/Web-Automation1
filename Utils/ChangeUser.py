__author__ = 'Eidan Wasser'
import time

from Utils import Config
from Login import Signup


def change_to_premium(isPremium=False):
    if isPremium == False: isPremium = "Free Account"
    else: isPremium = "Premium Account"
    Config.find_element(Config.openSettings).click()
    time.sleep(1)
    if Config.find_element(Config.settings_accountStatus).text == isPremium:
        if isPremium == "Free Account": change_user("premaut@any.do")
        else: change_user()

    else:
        Config.find_element(Config.overlay).click()
        Config.wait_for_element_visibility(Config.overlay, visible=False)

def change_user(email=None):
    if not Config.find_element(Config.signIn_alreadyMember).is_displayed():
        if not Config.is_element_present(Config.settingsPane):
            Config.find_element(Config.openSettings).click()
        Config.find_element(Config.settings_profile).click()
        Config.find_element(Config.profile_signOut).click()
        Config.wait_for_element_visibility(Config.signIn_alreadyMember)
    if email != None:
        Config.find_element(Config.signIn_alreadyMember).click()
        Config.wait_for_element_visibility(Config.signIn_inputEmail)
        Config.find_element(Config.signIn_inputEmail).clear()
        Config.find_element(Config.signIn_inputEmail).send_keys(email)
        Config.find_element(Config.signIn_inputPass).clear()
        Config.find_element(Config.signIn_inputPass).send_keys("123456")
        Config.find_element(Config.signIn_button).click()
        Config.wait_for_element(Config.main_AllTasks)
    else:
        s = Signup.SignUp("test")
        email = s.test()
        return email