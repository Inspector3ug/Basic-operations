#Code originally made by Inspector3ug
#https://github.com/Inspector3ug/Basic-operations
#Basic operations for linux

import os
import time
import sys
import webbrowser as wb

time.sleep(1)
print("Code by Inspector3ug")
time.sleep(3)
print(f"Welcome to Python {sys.version_info.major}.{sys.version_info.minor}!")
time.sleep(1.5)
print("List basic operations for Linux:")
print("1. Sleep ")
print("2. Shutdown")
print("3. Reboot")
print("4. Open GitHub ")
print(f"5. Exit from Python {sys.version_info.major}.{sys.version_info.minor}")
time.sleep(0.5)
work = input("Select your operation [1/2/3/4/5]: ")

if work == "1":
        print("Sleeping computer...")
        time.sleep(3)
        os.system("systemctl suspend" )

if work == "2":
    print("Shutdowning computer...")
    time.sleep(3)
    os.system("systemctl poweroff")

if work == "3":
    print("Restarting computer...")
    time.sleep(3)
    os.system("systemctl reboot")

if work == "4":
    print("Opening GitHub... ")
    time.sleep(3)
    wb.open("https://github.com/Inspector3ug/Basic-operations")

if work == "5":
    print("Goodbye!")
    time.sleep(3)
    sys.exit()

else:
    print("Invalid input! You need to enter the choice correctly! [1/2/3/4/5]")
    time.sleep(3)
    sys.exit()
