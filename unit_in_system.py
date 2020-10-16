import requests
from datetime import datetime
import pytz
import time

class unit_in_system:

    def getTimeNow(self):
        tz_PS = pytz.timezone('US/Pacific')
        datetime_PS = datetime.now(tz_PS)
        pst = datetime_PS.strftime("%H%M%S")
        # pstRealtime = datetime_PS.strftime("%H:%M:%S")
        pstimes = int(pst)
        print("Unit in system: " + pst)

        if pstimes >= 235500 and pstimes <= 235500:
            print("It's time...")
            return True
        else:
            return False

    def processAPI(self):
        url = 'https://index.scrapcatapp.com/api/units-in-system-process'
        response = requests.get(url)
        print(response)
        sleepMe = 60 * 30  # sleep 30 minutes
        time.sleep(sleepMe)
        print("The auto report processed is done, the system will become reactive after 30 minutes.")

    def Start(self):

        print("Started... Unit in system")

        while(True):

            time.sleep(1)
            res = self.getTimeNow()
            if res == True:
                self.processAPI()
