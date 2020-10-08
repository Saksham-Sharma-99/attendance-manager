import pyautogui as pg
import os
import time
import pandas as pd
from pandas import DataFrame
from datetime import datetime, timedelta

filePath = 'open /Applications/Microsoft\ Teams.app'
openingTime = 30   #seconds(max time)
timeTable = pd.read_csv('timeTable.csv')

right = pg.size().width
bottom = pg.size().height

classes = DataFrame(timeTable,columns=['Class_Name','Time'])
indices = [day for day in timeTable['Day']]
classes.index = indices
classes.index.name = 'Day'



def openTeams():
    today = datetime.today().strftime('%A')
    timeStart = (datetime.today() +timedelta(minutes = 7)).strftime('%I:%M %p')
    timeEnd = (datetime.now() + timedelta(hours = 1) +timedelta(minutes = 7)).strftime('%I:%M %p')
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



def locateClass():
    today = datetime.today().strftime('%A')
    timeStart = (datetime.today() +timedelta(minutes = 5)).strftime('%I:%M %p')
    timeEnd = (datetime.now() + timedelta(hours = 1) +timedelta(minutes = 5)).strftime('%I:%M %p')

    lectures = classes.loc[today]
    currentLec = lectures[lectures['Time']==(timeStart+'-'+timeEnd)]

    if not currentLec.empty:
        print(currentLec.loc[ today , 'Class_Name'])
        openClass(currentLec.loc[ today , 'Class_Name'])
    else:
        time.sleep(30)
        locateClass()



def openClass(className):
    pg.hotkey('tab')
    pg.hotkey('tab')
    pg.write(className , interval = 0.15)
    pg.keyDown('shift')
    pg.press('down')
    pg.keyUp('shift')
    pg.hotkey('enter')
    locateMeeting()



def locateMeeting():
    time.sleep(10)
    pg.moveTo(right-80 , 16, duration = 1)
    pg.click(right-80 , 10)

    time.sleep(0.25)
    for i in range(10):
        pg.hotkey('tab')

    pg.hotkey('enter')
    pg.hotkey('enter')
    time.sleep(0.25)
    pg.hotkey('tab')
    time.sleep(0.25)
    pg.hotkey('tab')
    time.sleep(0.25)

    pg.hotkey('enter')
    joinClass()





today = datetime.today().strftime('%A')
lectures = [i for i,day in enumerate(classes.loc[today])]

def joinClass():
    global lectures
    time.sleep(10)
    pg.hotkey('tab')
    time.sleep(0.25)
    pg.hotkey('return')
    time.sleep(openingTime)

    pg.hotkey('tab')
    pg.hotkey('tab')
    time.sleep(0.25)
    pg.hotkey('enter')

    time.sleep(0.25)
    for i in range(9):
        pg.hotkey('tab')

    time.sleep(0.25)
    pg.hotkey('enter')
    lectures.pop()


while(len(lectures)>0):
    print("lectures left = " + str(len(lectures)))
    openTeams()
