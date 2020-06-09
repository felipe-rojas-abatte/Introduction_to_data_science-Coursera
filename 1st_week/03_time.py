import datetime as dt
import time as tm

print(tm.time()) ## Imprime el tiempo transcurrido en segs desde 1 enero de 1970

dtnow = dt.datetime.fromtimestamp(tm.time()) #Convert the timestamp to datetime.
print(dtnow)
#dtnow.year, dtnow.month, dtnow.day, dtnow.hour, dtnow.minute, dtnow.second # get year, month, day, etc.from a datetime

delta = dt.timedelta(days = 100) # create a timedelta of 100 days
delta
