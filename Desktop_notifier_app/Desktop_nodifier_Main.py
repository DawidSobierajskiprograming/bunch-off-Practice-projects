import datetime
import time
import requests
from plyer import notification

FoxHoledata = None

try:

    FoxHoledata= requests.get("https://war-service-live.foxholeservices.com/api/worldconquest/warReport/LochMorHex")

except:
    print ("Something went wrong with requesting the data")


if (FoxHoledata != None):
    notification.notify(
        title = "FoxHole War status on {}".format(datetime.date.today()),

        message = 
    )