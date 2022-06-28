import datetime
x = datetime.datetime.now()
print(type(x))
print(x)
print(x.timestamp())
import time
time.sleep(5)
print(x.timestamp())
