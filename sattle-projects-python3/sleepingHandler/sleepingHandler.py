import threading
import time

from onCommand.onCommandHandler import *
from serialHandler.serialHandler import *

def sum():
    while(True):
        run()

def run():
    time.sleep(0.1)
    tilt = getTilt()

    try:
        if tilt == '0':
            print('뭐야!')
        else:
            print('꿈뻑...')
    except:
        pass
    
        
#t = threading.Thread(target=sum, args=())
#t.start()
