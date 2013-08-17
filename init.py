import praw
import warnings
import logging
from cmds import *

#get rid of warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
warnings.filterwarnings("ignore", category=ResourceWarning)

#preliminary setup
uAgent = ("Reddit console 1.0 by /u/swarage"
          "github.com/swarage/reddit-console")
r = praw.Reddit(user_agent=uAgent)
logger = logging.getLogger('reddit-console')
logging.basicConfig(format='%(message)s',
                            level=logging.NOTSET)
formatter = logging.Formatter('[%(asctime)s] %(levelname)s %(message)s')
fileHandler = logging.FileHandler('console_reddit.log')
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)

#setup interpreter
exitCodes = ("exit", "Exit", "quit", "Quit", "e", "E", "q", "Q")

def parseCommand(cmd):
    if cmd in exitCodes:
        return cmd
    else:
        try:
            legalCmds[cmd](r)
        except AttributeError:
            print("you aren't logged in")
            return "you aren't logged in"
        else:
            print("misspelled command")
            return "you aren't logged in"
