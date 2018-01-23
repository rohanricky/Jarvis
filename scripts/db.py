'''
Still need to specify schema
Under development
'''

import sqlite3
import re
# Todo -> schedule reminders, todo lists
class DB:

	def __init__(self,dbname):
		self.dbname = dbname
		self.conn = sqlite3.connect(dbname)
		cmd = "CREATE TABLE IF NOT EXISTS reminders (description text)"
		time= "CREATE TABLE IF NOT EXISTS deadline (description text)"
		self.conn.execute(cmd)
		self.conn.execute(time)
		self.conn.commit()

	def add_reminder(self,reminder_name):
		time = re.findall('\d+',reminder_name)
		reminder=re.sub(r'\d+',"",reminder_name)
		cmd = "INSERT INTO reminders (description) VALUES (?)"
		arg = (reminder, )
		self.conn.execute(cmd,arg)
		self.conn.commit()

	def delete_reminder(self,reminder_name):
		cmd ="DELETE FROM reminders WHERE description= (?)"
		arg = (reminder_name, )
		self.conn.execute(cmd,arg)
		self.conn.commit()

	def delete_all(self):
		cmd="DELETE FROM reminders WHERE description > -1;"
		self.conn.execute(cmd)
		self.conn.commit()

	def reminders_list(self):
		cmd = "SELECT description FROM reminders"
		return [x[0] for x in self.conn.execute(cmd)]
