import logging
import threading
from datetime import datetime
import time

from daily_report import daily_report
from lot_bid_report import lot_bid_report

dreport = daily_report()
lbreport = lot_bid_report()

def print_time_1():
    dreport.Start()

def print_time_2():
    lbreport.Start()

try: 

   t1 = threading.Thread(target=print_time_1)
   t2 = threading.Thread(target=print_time_2)

   # starting thread 1
   t1.start()
   # starting thread 2
   t2.start()

   # wait until thread 1 is completely executed
   t1.join()
   # wait until thread 2 is completely executed
   t2.join()
except:
   print("Error: unable to start thread")
