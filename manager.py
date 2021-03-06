import pyautogui as pg
import os
import sys
from sys import platform
import time
import pandas as pd
from pandas import DataFrame
from datetime import datetime, timedelta

pg.FAILSAFE = False

filePath = 'open /Applications/Microsoft\ Teams.app'
openingTime = 20   #seconds(max time)
timeTable = pd.read_csv('timeTable.csv')
minForDisconnect = 4

right = pg.size().width
bottom = pg.size().height

classes = DataFrame(timeTable,columns=['Class_Name','Time'])
indices = [day for day in timeTable['Day']]
classes.index = indices
classes.index.name = 'Day'

hours = datetime.now().hour
today = ''
if int(hours)>17:
    today = (datetime.today()+timedelta(days=1)).strftime('%A')
else:
    today = datetime.today().strftime('%A')


def openTeams():
    global today

    if datetime.now().hour > 18 and datetime.now().second < 2:
        print('y')
        os.execv(sys.executable, ['python'] + [sys.argv[0]])

    if not isClassOpen():
        timeStart = (datetime.today() +timedelta(minutes = 3)).strftime('%I:%M %p')
        timeEnd = (datetime.now() + timedelta(hours = 1) +timedelta(minutes = 3)).strftime('%I:%M %p')
        lectures = classes.loc[today]
        currentLec = lectures[lectures['Time']==(timeStart+'-'+timeEnd)]

        if not currentLec.empty:
            os.system(filePath)
            time.sleep(openingTime)
            pg.moveTo(right-80 , 16)
            pg.click(right-80 , 10)
            locateClass()
        else:
            time.sleep(30)
            pg.moveTo(20 , 16,duration = 1)
            pg.moveTo(right-20 , bottom-16,duration = 1)
            openTeams()
    else:
        locateClass()



def locateClass():
    global today
    if not isClassOpen():
        timeStart = (datetime.today() +timedelta(minutes = 2)).strftime('%I:%M %p')
        timeEnd = (datetime.now() + timedelta(hours = 1) +timedelta(minutes = 2)).strftime('%I:%M %p')
        lectures = classes.loc[today]
        currentLec = lectures[lectures['Time']==(timeStart+'-'+timeEnd)]
        if not currentLec.empty:
            print(currentLec.loc[ today , 'Class_Name'])
            openClass(currentLec.loc[ today , 'Class_Name'])
        else:
            time.sleep(30)
            locateClass()
    else:
        timeStart = (datetime.today()+timedelta(minutes = minForDisconnect)).strftime('%I:%M %p')
        timeEnd = (datetime.now() + timedelta(hours = 1)+timedelta(minutes = minForDisconnect)).strftime('%I:%M %p')
        lectures = classes.loc[today]
        currentLec = lectures[lectures['Time']==(timeStart+'-'+timeEnd)]
        if not currentLec.empty:
            print(currentLec.loc[ today , 'Class_Name'])
            disconnectClass()
            openClass(currentLec.loc[ today , 'Class_Name'])
        else:
            time.sleep(30)
            locateClass()



def openClass(className):
    pg.hotkey('tab')
    pg.hotkey('tab')
    pg.write(className , interval = 0.08)
    pg.keyDown('shift')
    pg.press('down')
    pg.keyUp('shift')
    pg.hotkey('enter')
    locateMeeting()



def locateMeeting():
    time.sleep(10)
    pg.moveTo(right-80 , 16, duration = 1)
    pg.click(right-80 , 10)

    if not class_already_started():
        for i in range(10):
            pg.hotkey('tab')
        time.sleep(0.25)
        pg.hotkey('enter')
        pg.hotkey('enter')
        time.sleep(0.25)
        pg.hotkey('tab')
        time.sleep(0.25)
        pg.hotkey('tab')
        time.sleep(0.25)

        pg.hotkey('enter')
        joinClass()
    else:
        pg.click()
        time.sleep(5)
        for i in range(5):
            pg.hotkey('tab')

        time.sleep(0.25)
        pg.hotkey('enter')
        lectures = lectures[1:]



def class_already_started():
    r = pg.locateCenterOnScreen('join_btn.png' , confidence = 0.9)

    if r != None:
        if platform == "darwin":
            pg.moveTo(r.x/2 , r.y/2)
            pg.click()
        elif platform == "win32":
            pg.moveTo(r.x , r.y)
            pg.click()
        return True
    else:
        return False




def isClassOpen():
    minutes = datetime.now().minute
    timeStart = (datetime.today() -timedelta(minutes = minutes)).strftime('%I:%M %p')
    timeEnd = (datetime.today() +timedelta(hours = 1) - timedelta(minutes = minutes)).strftime('%I:%M %p')
    lectures = classes.loc[today]
    currentLec = lectures[lectures['Time']==(timeStart+'-'+timeEnd)]

    return not currentLec.empty




lectures = classes.loc[today]



def joinClass():
    global lectures
    time.sleep(10)
    for i in range(10):
        pg.hotkey('tab')
    time.sleep(0.25)
    pg.hotkey('return')
    time.sleep(5)

    pg.hotkey('tab')
    pg.hotkey('tab')
    time.sleep(0.25)
    pg.hotkey('enter')

    time.sleep(0.25)
    for i in range(9):
        pg.hotkey('tab')

    time.sleep(0.25)
    pg.hotkey('enter')
    lectures = lectures[1:]
    time.sleep(3)



def disconnectClass():
    r = pg.locateCenterOnScreen('disconnect.png' , confidence = 0.9)
    if r != None:
        if platform == "darwin":
            pg.moveTo(r.x/2 , r.y/2)
            pg.click()
        elif platform == "win32":
            pg.moveTo(r.x , r.y)
            pg.click()
    pg.moveTo(right-80 , 16)
    pg.click(right-80 , 10)


while(len(lectures)>0):
    print("lectures left = "+str(len(lectures)))
    print(lectures)
    openTeams()
