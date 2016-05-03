import getList
import subprocess
from say import *

def notify():
    for i in range(100):
        message = "Tickets are up, bitch"
        subprocess.Popen(['notify-send', message])

l = getList.getList()
threaterList = ["INOX: GVK One, Banjara Hills", "PVR: Inorbit, Cyberabad", "PVR: Forum Sujana Mall, Kukatpally"]

for i in threaterList:
    if i in l:
        notify()
