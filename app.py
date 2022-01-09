import pyttsx3
import datetime

TakeHour = int(input("Enter Hour : "))
TakeMinute = int(input("Enter Minute : "))
TakeFormat = input("am / pm : ")
TakeCommand = input("Write Your Command Here : ")
print("Task Reminder Set Successfully")

if TakeFormat == "pm" :
    TakeHour += 12

while True :
   if TakeHour == datetime.datetime.now().hour and TakeMinute == datetime.datetime.now().minute :
      angela = pyttsx3.init()
      angela.say(TakeCommand)
      angela.runAndWait()
