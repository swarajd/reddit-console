from init import *

#login
uname, logged_in = login()
#setup prompt
if logged_in:
    selfInfo = r.get_redditor(uname)
    prompt = uname + " (" + str(selfInfo.link_karma) + "|" + str(selfInfo.comment_karma) + "): "
    print(prompt)
else:
    prompt = "Guest: "
    
#start interpreter
inp = ""
while inp not in exitCodes:
    inp = input(prompt)
    parseCommand(inp)
