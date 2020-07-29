import requests
from datetime import datetime
import pytz
import time

def getTimeNow():
    tz_PS = pytz.timezone('US/Pacific')
    datetime_PS = datetime.now(tz_PS)
    pst = datetime_PS.strftime("%H%M%S")
    pstRealtime = datetime_PS.strftime("%H:%M:%S")
    pstimes = int(pst)
    #print(pstimes)
    #print(pstRealtime)

    if pstimes >= 235500 and pstimes <= 235500:
        print("It's time...")
	print(pstimes)
        print(pstRealtime)
        return True
    else:
        #print("No, It's not time")
        return False

def processAPI():
    url = 'https://index.scrapcat.net/v2/daily-reports-process'
    response = requests.get(url)
    print(response)
    sleepMe = 60 * 30 # sleep 30 minutes
    time.sleep(sleepMe)
    print("The auto report processed is done, the system will become reactive after 30 minutes.")

print("Started... v2")
while(True):

    time.sleep(1)
    res = getTimeNow()
    if res == True:
        processAPI()

