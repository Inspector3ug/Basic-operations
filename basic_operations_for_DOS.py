#Code originally made by Inspector3ug
#https://github.com/Inspector3ug/Basic-operations
#Basic operations for windows 

import os
import time
import sys
import ctypes
import webbrowser as wb

def isAdmin():
    try:
        is_admin = (os.getuid() == 0)
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin

time.sleep(1)
print("Code by Inspector3ug")
time.sleep(3)
print(f"Welcome to Python {sys.version_info.major}.{sys.version_info.minor}!")
time.sleep(1.5)
print("List basic operations for Windows:")
print("1. Sleep (This command require run as administrator)")
print("2. Shutdown")
print("3. Reboot")
print("4. Open GitHub ")
print(f"5. Exit from Python {sys.version_info.major}.{sys.version_info.minor}")
time.sleep(0.5)
work = input("Select your operation [1/2/3/4/5]: ")

if work == "1":
    print(f"Checking if you're running Python {sys.version_info.major}.{sys.version_info.minor} as administrator...")
    time.sleep(2)
    if isAdmin():
        print(f"You're running Python {sys.version_info.major}.{sys.version_info.minor} as administrator. Sleeping computer...")
        time.sleep(3)
        os.system("powercfg -hibernate off")
        time.sleep(0.3)
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    else:
        print(f"You need to run Python {sys.version_info.major}.{sys.version_info.minor} as administrator!")
        time.sleep(1)
        print(f"Exiting Python {sys.version_info.major}.{sys.version_info.minor}...")
        time.sleep(3)
        sys.exit()

if work == "2":
    print("Shutdowning computer...")
    time.sleep(3)
    os.system("shutdown.exe -s -t 00")

if work == "3":
    print("Restarting computer...")
    time.sleep(3)
    os.system("shutdown.exe -r -t 00")

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
