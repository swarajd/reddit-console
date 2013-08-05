from init import *
from cmds import *

#login
def login():
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
    return logged_in,username
    
logged_in, uname = login()

#setup prompt
if logged_in:
    selfInfo = r.get_redditor(uname)
    prompt = uname + " (" + str(selfInfo.link_karma) + "|" + str(selfInfo.comment_karma) + "): "
else:
    prompt = "Guest: "
    
#start interpreter
if __name__ == "__main__":
    inp = ""
    while inp not in exitCodes:
        inp = input(prompt)
        parseCommand(inp)
