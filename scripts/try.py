from db import DB
import os

base=os.getcwd()
db = DB(base+"/reminder.sqlite")
db.add_reminder("Remind 430")
print(db.reminders_list())
