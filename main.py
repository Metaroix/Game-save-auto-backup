import os
import shutil
import getpass
import time
import keyboard

username = getpass.getuser()

source = f"C:\\Users\\{username}\\Appdata\\LocalLow\\default"

destination = "C:\\Users\\AceNo\\OneDrive\\Desktop\\to"

timer = int(input("How frequent in minutes: "))
timer = timer*60
def restore():
    shutil.copy(destination, source)
    print ("files have been restored to the Game Folder")
x=0
while True:
    time.sleep(timer)
    shutil.copy(source, destination)
    x=x+1
    print(f"The game files have been backup {x} times")
    if os.scandir(destination)>3:
        os.remove(f"destination\\default")
    keyboard.add_hotkey('ctrl + shift + r', restore)

