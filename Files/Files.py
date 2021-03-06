__author__ = 'Eidan Wasser'
import unittest

import AddPic
import DeletePic
import PreviewPic
import AddAudio
import DeleteAudio
import AddVideo
import PreviewVideo
import DeleteVideo
import GoogleDrive
import AddNote, EditNote
import Dropbox

def files():
    n = unittest.TestSuite()

    n.addTest(AddPic.AddPic("test"))
    n.addTest(PreviewPic.PreviewPic("test"))
    n.addTest(DeletePic.DeletePic("test"))
    n.addTest(AddAudio.AddAudio("test"))
    n.addTest(DeleteAudio.DeleteAudio("test"))
    n.addTest(AddVideo.AddVideo("test"))
    n.addTest(PreviewVideo.PreviewVideo("test"))
    n.addTest(DeleteVideo.DeleteVideo("test"))
    n.addTest(AddNote.AddNote("test"))
    n.addTest(EditNote.EditNote("test"))
    n.addTest(GoogleDrive.GoogleDrive("test"))
    n.addTest(Dropbox.AddFromDropbox("test"))
    return n
