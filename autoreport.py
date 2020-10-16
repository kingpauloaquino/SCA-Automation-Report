import logging
import threading
from datetime import datetime
import time

from daily_report import daily_report
from lot_bid_report import lot_bid_report
from unit_in_system import unit_in_system

dreport = daily_report()
lbreport = lot_bid_report()
unitreport = unit_in_system()

def print_time_1():
    dreport.Start()

def print_time_2():
    lbreport.Start()

def print_time_3():
    unitreport.Start()

try: 

   t1 = threading.Thread(target=print_time_1)
   t2 = threading.Thread(target=print_time_2)
   t3 = threading.Thread(target=print_time_3)

   t1.start()
   t2.start()
   t3.start()

   t1.join()
   t2.join()
   t3.join()
except:
   print("Error: unable to start thread")
