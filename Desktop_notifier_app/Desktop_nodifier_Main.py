import datetime
import time
import requests
from plyer import notification
import json

FoxHoledata = None
Foxholemaps = ["StonecradleHex", "AllodsBightHex", "TempestIslandHex", "GreatMarchHex", "MarbanHollow", "ViperPitHex", "ShackledChasmHex", "HeartlandsHex", "DeadLandsHex", "LinnMercyHex", "EndlessShoreHex", "GodcroftsHex", "FishermansRowHex", "WestgateHex", "ReachingTrailHex", "UmbralWildwoodHex", "OarbreakerHex", "CallahansPassageHex", "DrownedValeHex", "FarranacCoastHex", "MooringCountyHex", "WeatheredExpanseHex", "LochMorHex"]
try:

    FoxHoledata= "https://war-service-live.foxholeservices.com/api/worldconquest/warReport/{}"

except:
    print ("Something went wrong with requesting the data")

def totalcasulties():
    totalcasulties = 0
    for i in Foxholemaps:
        a = FoxHoledata.format(i)
        Foxholeget = requests.get(a)
        Foxholejson = Foxholeget.json()
        totalcasulties = Foxholejson["colonialCasualties"] + Foxholejson["wardenCasualties"] + totalcasulties
    print (totalcasulties)
    return totalcasulties

print(1)
totalcasulties()