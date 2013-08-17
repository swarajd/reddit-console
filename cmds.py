import praw
import warnings
import logging
from init import *

#get rid of warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
warnings.filterwarnings("ignore", category=ResourceWarning)

def getSaved(r):
    saved = r.user.get_saved()
    for i in saved:
        print(i)

def sendMsg(r):
    recipient = input("recipient> ")
    subject = input("subject> ")
    message = input("message> ")
    r.send_message(recipient,subject,message)



legalCmds = {"saved": getSaved, "send": sendMsg}
