__author__ = 'Eidan Wasser'

import unittest
import GooglePlus, Facebook, SignIn, FacebookSignIn, GooglePlusSignIn

def login():
    n = unittest.TestSuite()
    n.addTest(GooglePlus.GooglePlus("test"))
    n.addTest(Facebook.Facebook("test"))
    n.addTest(SignIn.SignIn("test"))
    n.addTest(FacebookSignIn.FacebookSignIn("test"))
    n.addTest(GooglePlusSignIn.GooglePlusSignIn("test"))
    return n
