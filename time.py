import time
import datetime

# print (time.time())
# print (time.clock())
# print (time.gmtime())
# print (time.localtime())
localtimes=time.localtime()
print (time.mktime(localtimes))
time.sleep(2)
localtimes=time.localtime()
print (time.mktime(localtimes))

T=datetime.datetime(2016,9,12,12,25)
T1=datetime.datetime(time.mktime(time.localtime))
T2=datetime.timedelta(days=100)
print (T,T1,T2,T1+T)
