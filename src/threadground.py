import threading
from threading import Thread
import os
from playground import Looper

def taco():
    # while (True):
    print("Taco")


def runrun():
    # while (True):
        print(687)
        pass
b = threading.Thread(target=runrun())
b2 = threading.Thread(target=taco())
b.start()
b2.start()