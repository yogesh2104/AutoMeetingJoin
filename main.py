import datetime
from selenium import webdriver
import schedule
from classLink import *
import timetable


try:
    driver = webdriver.Chrome('C:\\Users\\Yogesh Singh\\Desktop\\Project\\AutoJoinMetting\\driver\\chromedriver.exe')
except Exception:
    print('check internet connetion',error)
currtent_time = datetime.datetime.now()
# print(currtent_time)

def monday():
    """[summary]
    here schedule library are beacuse we want to join a class 
    every day or any particular time/day in week. 
    """
    schedule.every().monday.at(firstClass).do(EnglishClass())
    schedule.every().monday.at(secondClass).do(OopsClass())
    schedule.every().monday.at(thirdClass).do(dbmsClass())
    schedule.every().monday.at(fourthClass).do(DataStrClass())
    schedule.every().monday.at(fifthClass).do(cybersecClass())
    schedule.every().monday.at(fifthClass).do(automataClass())
    schedule.every().monday.at(fifthClass).do(rpaClass())

def monday():
    """[summary]
    here schedule library are beacuse we want to join a class 
    every day or any particular time/day in week. 
    """
    schedule.every().monday.at(firstClass).do(EnglishClass())
    schedule.every().monday.at(secondClass).do(OopsClass())
    schedule.every().monday.at(thirdClass).do(dbmsClass())
    schedule.every().monday.at(fourthClass).do(DataStrClass())
    schedule.every().monday.at(fifthClass).do(cybersecClass())
    schedule.every().monday.at(fifthClass).do(automataClass())
    schedule.every().monday.at(fifthClass).do(rpaClass())

def tuesday():
    """[summary]
    here schedule library are beacuse we want to join a class 
    every day or any particular time/day in week. 
    """
    schedule.every().monday.at(firstClass).do(EnglishClass())
    schedule.every().monday.at(secondClass).do(OopsClass())
    schedule.every().monday.at(thirdClass).do(dbmsClass())
    schedule.every().monday.at(fourthClass).do(DataStrClass())
    schedule.every().monday.at(fifthClass).do(cybersecClass())
    schedule.every().monday.at(fifthClass).do(automataClass())
    schedule.every().monday.at(fifthClass).do(rpaClass())

def wednesday():
    """[summary]
    here schedule library are beacuse we want to join a class 
    every day or any particular time/day in week. 
    """
    schedule.every().monday.at(firstClass).do(EnglishClass())
    schedule.every().monday.at(secondClass).do(OopsClass())
    schedule.every().monday.at(thirdClass).do(dbmsClass())
    schedule.every().monday.at(fourthClass).do(DataStrClass())
    schedule.every().monday.at(fifthClass).do(cybersecClass())
    schedule.every().monday.at(fifthClass).do(automataClass())
    schedule.every().monday.at(fifthClass).do(rpaClass())

def thursday():
    """[summary]
    here schedule library are beacuse we want to join a class 
    every day or any particular time/day in week. 
    """
    schedule.every().monday.at(firstClass).do(EnglishClass())
    schedule.every().monday.at(secondClass).do(OopsClass())
    schedule.every().monday.at(thirdClass).do(dbmsClass())
    schedule.every().monday.at(fourthClass).do(DataStrClass())
    schedule.every().monday.at(fifthClass).do(cybersecClass())
    schedule.every().monday.at(fifthClass).do(automataClass())
    schedule.every().monday.at(fifthClass).do(rpaClass())

def friday():
    """[summary]
    here schedule library are beacuse we want to join a class 
    every day or any particular time/day in week. 
    """
    schedule.every().monday.at(firstClass).do(EnglishClass())
    schedule.every().monday.at(secondClass).do(OopsClass())
    schedule.every().monday.at(thirdClass).do(dbmsClass())
    schedule.every().monday.at(fourthClass).do(DataStrClass())
    schedule.every().monday.at(fifthClass).do(cybersecClass())
    schedule.every().monday.at(fifthClass).do(automataClass())
    schedule.every().monday.at(fifthClass).do(rpaClass())

def saturday():
    """[summary]
    here schedule library are beacuse we want to join a class 
    every day or any particular time/day in week. 
    """
    schedule.every().monday.at(firstClass).do(EnglishClass())
    schedule.every().monday.at(secondClass).do(OopsClass())
    schedule.every().monday.at(thirdClass).do(dbmsClass())
    schedule.every().monday.at(fourthClass).do(DataStrClass())
    schedule.every().monday.at(fifthClass).do(cybersecClass())
    schedule.every().monday.at(fifthClass).do(automataClass())
    schedule.every().monday.at(fifthClass).do(rpaClass())


while True:
    schedule.run_pending()
    time.sleep(1)

day = (currtent_time.strftime("%a"))
print(day)

if day=="Mon":
    monday()

elif day =="Tue":
    tuesday()

elif day =="Wed":
    wednesday()

elif day =="Thu":
    thursday()

elif day =="Fri":
    friday()

elif day =="Sat":
    saturday()
else:
    print("Its sunday!!!!")