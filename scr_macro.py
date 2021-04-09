import pyautogui
import keyboard
import os.path
from os import path
from datetime import datetime
from datetime import date
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from pydrive.settings import InvalidConfigError


# Getting access to google drive
gauth = GoogleAuth()
auth_url = gauth.GetAuthUrl()
drive = GoogleDrive(gauth)
ID = 'YOUR ID'

while True:
    if keyboard.is_pressed('q'):
        now = datetime.now()
        today = date.today()
        dt_string = now.strftime("%d%m%Y%H%M%S")    # Getting current time
        dt_string = dt_string + ".png"
        d3 = today.strftime("%d%m%y")
        myScreenshot = pyautogui.screenshot()       # Making screenshot
        if path.exists('Screenshots') == True:      # Checking if primary path exists
            if path.exists('Screenshots\%s'% (d3)) == True:     #Checking if secondary path exists
                myScreenshot.save(r'Screenshots\%s\%s'% (d3,dt_string))     #Saving screenshot
                try:
                    gfile = drive.CreateFile({'parents': [{'id': ID}]})        # Getting id of your google drive
                    gfile.SetContentFile(r'Screenshots\%s\%s'% (d3,dt_string))      # Saving file inside your google drive
                    gfile.Upload()  # Upload the file to google drive
                    print("Success")
                except InvalidConfigError:
                    print ("InvalidConfigError")
                    pass
                #https://d35mpxyw7m7k7g.cloudfront.net/bigdata_1/Get+Authentication+for+Google+Service+API+.pdf
            else:
                os.mkdir('Screenshots\%s'% (d3))    # if path didn't exist before it creates secondary path
                myScreenshot.save(r'Screenshots\%s\%s' % (d3,dt_string))       # Saving screenshot
                try:
                    gfile = drive.CreateFile({'parents': [{'id': ID}]})        # Getting id of your google drive
                    gfile.SetContentFile(r'Screenshots\%s\%s'% (d3,dt_string))      # Saving file inside your google drive
                    gfile.Upload()  # Upload the file to google drive
                    print("Success")
                except InvalidConfigError:
                    print ("InvalidConfigError")
                    pass
        else:
            os.mkdir('Screenshots')             # if didn't exist it creates primary path
            os.mkdir('Screenshots\%s' % (d3))   # if didn't exist it creates secondary path
            myScreenshot.save(r'Screenshots\%s\%s' % (d3, dt_string))
            try:
                gfile = drive.CreateFile({'parents': [{'id': ID}]})  # Getting id of your google drive
                gfile.SetContentFile(r'Screenshots\%s\%s' % (d3, dt_string))  # Saving file inside your google drive
                gfile.Upload()  # Upload the file to google drive
                print("Success")
            except InvalidConfigError:
                print("InvalidConfigError")
                pass
