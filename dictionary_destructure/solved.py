object1 = {"key":"VUEwMDAwMDAxMDczOTgwMzc=",
          "offset":219438089,
          "partition":1,
          "timestamp":1593880887640,
          "topic":"clickstream",
          "value":"eyJkZXZpY2UiOiJBbmRyb2lkIiwiZWNvbW1lcmNlIjp7fSwiZXZlbnRfbmFtZSI6ImRlbGl2ZXJ5IiwiZXZlbnRfcHJldmlvdXNfdGltZXN0YW1wIjoxNTkzODgwODgyOTY0MjYyLCJldmVudF90aW1lc3RhbXAiOjE1OTM4ODA4ODc2MDUzMzcsImdlbyI6eyJjaXR5IjoiVmVybm9uIiwic3RhdGUiOiJUWCJ9LCJpdGVtcyI6W10sInRyYWZmaWNfc291cmNlIjoiZmFjZWJvb2siLCJ1c2VyX2ZpcnN0X3RvdWNoX3RpbWVzdGFtcCI6MTU5Mzg4MDg4Mjk2NDI2MiwidXNlcl9pZCI6IlVBMDAwMDAwMTA3Mzk4MDM3In0="}


# 1) using tuple comprehension unpack values
print(object1.keys()) # dict_keys(['key', 'offset', 'partition', 'timestamp', 'topic', 'value'])


key, offset, partition, timestamp, topic, value = (key for key in object1.values())
print(key) # VUEwMDAwMDAxMDczOTgwMzc=
print(offset) # 219438089
print(partition) # 1
print(topic) # clickstream
print(value) #eyJkZXZpY2UiOiJBbmRyb2lkI...

# 2) import datetime 
from datetime import datetime

# timestamp from DB is in nanoseconds and need to be converted to miliseconds
# else we will get an error as below
try:
    time = datetime.fromtimestamp(timestamp)
except Exception as e:
    print(e) # ValueError: year 52478 is out of range 

    
converted_time = datetime.fromtimestamp(timestamp/1000)
print(converted_time) # 2020-07-04 11:41:27.640000

# to further disect we need to convert it into a string as it is a datetime object1
print(type(converted_time)) # <class 'datetime.datetime'>

date, time= str(converted_time).split()
print(date) # 2020-07-04
print(time) # 11:41:27.640000

year,month, day = date.split('-')
print(year) # 2020
print(month) # 07
print(day) # 04

hour, minute, second = time.split(":")
print(hour) # 11
print(minute) #41
print(second) # 27.640000

