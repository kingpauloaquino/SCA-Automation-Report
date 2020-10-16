import requests
from datetime import datetime
import pytz
import time

class lot_bid_report:

    def getTimeNow(self):
        tz_PS = pytz.timezone('US/Pacific')
        datetime_PS = datetime.now(tz_PS)
        pst = datetime_PS.strftime("%H%M%S")
        # pstRealtime = datetime_PS.strftime("%H:%M:%S")
        pstimes = int(pst)
        print("Lot bid report: " + pst)

        if pstimes >= 235500 and pstimes <= 235500:
            print("It's time...")
            return True
        else:
            return False

    def processAPI(self):
        url = 'https://index.scrapcatapp.com/lot-bid-reports-process'
        response = requests.get(url)
        print(response)
        sleepMe = 60 * 30  # sleep 30 minutes
        time.sleep(sleepMe)
        print("The auto report processed is done, the system will become reactive after 30 minutes.")

    def Start(self):

        print("Started... lot bid report")

        while(True):

            time.sleep(1)
            res = self.getTimeNow()
            if res == True:
                self.processAPI()
