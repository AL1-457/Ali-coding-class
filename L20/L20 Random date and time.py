import random
import time

def getRandomeDate(startDate, endDate):
    print(f"Printing random date between {startDate} and {endDate}")
    randomGenerator = random.random()

    dateFormat = "%m/%d/%Y"
    starttime = time.mktime(time.strptime(startDate, dateFormat))
    endtime = time.mktime(time.strptime(endDate, dateFormat))

    randomTime = starttime + randomGenerator * (endtime - starttime)
    randomDate = time.strftime ( dateFormat, time.localtime(randomTime))

    return randomDate

result = getRandomeDate("4/23/2025", "1/31/2029")
print("Random Date =", result)