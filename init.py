import praw
import warnings
import logging

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

#setup login
def login():
    logged_in = False
    print("enter username or blank if you want to lurk")
    username = input("username > ")
    password = input("password > ")
    if username:
        logged_in = True
        try:
            r.login(username,password)
        except:
            print("wrong credentials")
            login()
    return username,logged_in


#setup interpreter
exitCodes = ("exit", "Exit", "quit", "Quit", "e", "E", "q", "Q")
legalCmds = ()
def parseCommand(cmd):
    if cmd in exitCodes:
        return cmd
    elif cmd in legalCmds:
        cmd()
    else:
        return "invalid command"
