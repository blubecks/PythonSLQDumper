#!/usr/bin/python
# Filename: dumper.py
# created by Andrea Beccaris
import sys, os, time, datetime
from termcolor import colored

class PythonSQLDumper:
	"""docstring for PythonSQLDumper"""
	def __init__(self):
		try:
			self.read_config()
		except Exception as e:
			raise e

	def read_config(self):
		"""Read the Database Config"""
		print colored('I\'m going to read the Config','yellow')
		try:
			with open("config") as f:
				data = f.readlines()
				for line in data:
					line.split(':')
				mydict = {a:b.strip('\'\n') for a,b in [line.split(':') for line in data]}
				self.host = mydict['DB_HOST']
				self.database = mydict['DB_DATABASE']
				self.username = mydict['DB_USERNAME']
				self.password = mydict['DB_PASSWORD']
		except Exception as e:
			raise e
		print colored('Config file parsed!','green')

	def dump_database(self):
		try:
			DATETIME = time.strftime('%Y%m%d-%H%M%S')
			dumpcmd = "mysqldump -u " + self.username + " -p" + self.password + " " + self.database + " > " + DATETIME + "-" + self.database + ".sql"
			print dumpcmd
			#os.system(dumpcmd)
		except Exception, e:
			raise e


if __name__ == '__main__':
	try:
		d = PythonSQLDumper()
	except Exception as e:
		print colored('Exception due to a wrong/missing config file','red')
		sys.exit(0)
	d.dump_database()
else:
	print 'I am being imported from another module'
