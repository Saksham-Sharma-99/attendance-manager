# attendance-manager
a python program that automatically helps automatically connect to a MS Teams meeting at scheduled time

all you have to do is add a csv file which contains your time table information and change the location to the MS Teams app as per your computer storage
keep following things in mind
1) column 'Class_Name' contains the name of your Team in MS Teams
2) column 'Time' should be filled in the similar way as in the timeTable.csv file , i.e., HH:MM AM/PM-HH:MM AM/PM
3) MS Teams should run in full screen (maximised form)

Note:
This program works on certain assumptions and only under those it will work properly
1) classes should be pre-scheduled , and are being recorded by the prof
2) no reaction of any kind on any class should be there
3) class should be scheduled on daily basis

Having said this, you have the option to manipulate the code as per your situation .
All you would need to change is the number of times 'tab' is pressed

pyautogui source : https://github.com/asweigart/pyautogui

feel free to contribute


to run the prgoram do the following steps:
1) cd over to the attendace manager folder
2) pip install pyautogui
3) pip install pandas
4) export PYTHONPATH="${PYTHONPATH}:/usr/local/lib/python3.8/site-packages:/usr/lib/python3.8/site-packages"
5) python manager.py
