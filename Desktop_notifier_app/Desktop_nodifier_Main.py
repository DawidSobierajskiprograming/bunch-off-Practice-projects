import datetime
import time
import requests
from plyer import notification
import json

c = 3
FoxHoledata = None
Foxholemaps = ["StonecradleHex", "AllodsBightHex", "TempestIslandHex", "GreatMarchHex", "MarbanHollow", "ViperPitHex", "ShackledChasmHex", "HeartlandsHex", "DeadLandsHex", "LinnMercyHex", "EndlessShoreHex", "GodcroftsHex", "FishermansRowHex", "WestgateHex", "ReachingTrailHex", "UmbralWildwoodHex", "OarbreakerHex", "CallahansPassageHex", "DrownedValeHex", "FarranacCoastHex", "MooringCountyHex", "WeatheredExpanseHex", "LochMorHex"]

FoxHoledata= "https://war-service-live.foxholeservices.com/api/worldconquest/warReport/{}"


def totalcasulties():
    totalcasulties = 0
    for i in Foxholemaps:
        a = FoxHoledata.format(i)
        try:
            Foxholeget = requests.get(a)
        except:
            print("Check your internet connection")
        Foxholejson = Foxholeget.json()
        totalcasulties = Foxholejson["colonialCasualties"] + Foxholejson["wardenCasualties"] + totalcasulties
    print (totalcasulties)
    return totalcasulties


totalcasulties()