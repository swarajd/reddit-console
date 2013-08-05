import praw
import getpass

#preliminary setup
uAgent = ("Reddit console 1.0 by /u/swarage"
          "github.com/swarage/reddit-console")
r = praw.Reddit(user_agent=uAgent)

#login step
print("enter username or blank if you want to lurk")
username = input("username > ")
password = getpass.getpass("password > ")

logged_in = False
if username:
    logged_in = True


