import os
import sys
import psutil
import getpass

USER_NAME = getpass.getuser()

def add_to_startup(file_path=""):
    if file_path == "":
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
            os.chdir(application_path)
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'start "" %s' % application_path)

print("-----------------------------")
print("hello")
print("-----------------------------")

def Kill_ArmourySwAgent():
    killProcessName = ['ArmourySwAgent.exe']
    Count = 0
    while Count < 20:
        Count = Count +1
        print('Count : {}'.format(Count))
        for p in psutil.process_iter():
            for kpn in killProcessName:
                if p.name() == kpn:
                    print(p.kill)
                    print("Kill 'ArmourySwAgent.exe'")
                    os.system("pause")
        else:
            print("Not Found 'ArmourySwAgent.exe'")    
    os.system("pause")

Kill_ArmourySwAgent()