object1 = {
    "key":"VUEwMDAwMDAxMDczOTgxNTk=",
    "offset":219438114,
    "partition":1,
    "timestamp":1593880894803,
    "topic":"clickstream",
    "value":"eyJkZXZpY2UiOiJtYWNPUyIsImVjb21tZXJjZSI6e30sImV2ZW50X25hbWUiOiJtYWluIiwiZXZlbnRfdGltZXN0YW1wIjoxNTkzODgwODk0Nzg5NTc5LCJnZW8iOnsiY2l0eSI6Ikxha2V3b29kIiwic3RhdGUiOiJDTyJ9LCJpdGVtcyI6W10sInRyYWZmaWNfc291cmNlIjoieW91dHViZSIsInVzZXJfZmlyc3RfdG91Y2hfdGltZXN0YW1wIjoxNTkzODgwODk0Nzg5NTc5LCJ1c2VyX2lkIjoiVUEwMDAwMDAxMDczOTgxNTkifQ=="}

object2 = {
    "key":"VUEwMDAwMDAxMDczNzMwMDA=",
    "offset":219246323,
    "partition":0,
    "timestamp":1593880188213,
    "topic":"clickstream",
    "value":"eyJkZXZpY2UiOiJpT1MiLCJlY29tbWVyY2UiOnsicHVyY2hhc2VfcmV2ZW51ZV9pbl91c2QiOjk0NS4wLCJ0b3RhbF9pdGVtX3F1YW50aXR5IjoxLCJ1bmlxdWVfaXRlbXMiOjF9LCJldmVudF9uYW1lIjoiZmluYWxpemUiLCJldmVudF9wcmV2aW91c190aW1lc3RhbXAiOjE1OTM4ODAwNTQ3ODM3MzksImV2ZW50X3RpbWVzdGFtcCI6MTU5Mzg4MDE4ODE5MzM5NCwiZ2VvIjp7ImNpdHkiOiJJbmRpYW5hcG9saXMiLCJzdGF0ZSI6IklOIn0sIml0ZW1zIjpbeyJpdGVtX2lkIjoiTV9TVEFOX0YiLCJpdGVtX25hbWUiOiJTdGFuZGFyZCBGdWxsIE1hdHRyZXNzIiwiaXRlbV9yZXZlbnVlX2luX3VzZCI6OTQ1LjAsInByaWNlX2luX3VzZCI6OTQ1LjAsInF1YW50aXR5IjoxfV0sInRyYWZmaWNfc291cmNlIjoiZmFjZWJvb2siLCJ1c2VyX2ZpcnN0X3RvdWNoX3RpbWVzdGFtcCI6MTU5Mzg3ODE3Njg5MDUyNywidXNlcl9pZCI6IlVBMDAwMDAwMTA3MzczMDAwIn0="}


from datetime import datetime

timestamp1 = object1["timestamp"] / 1000
timestamp2 = object2["timestamp"] / 1000

timediff = datetime.fromtimestamp(timestamp1) - datetime.fromtimestamp(timestamp2)
print(timediff) # 0:11:46.590000

# remember to convert it to string 
print(type(timediff)) # <class 'datetime.timedelta'>

# unpack values
hour, minute, second = str(timediff).split(":") # (hour, minute, second) = ('0', '11', '46.590000') 


print(f"Time difference between object1 and object2 are {hour} hour(s), {minute} minute(s), {second.split('.')[0]} second(s), and {second.split('.')[1]} microseconds")
# Time difference between object1 and object2 are 0 hour(s), 11 minute(s), 46 second(s), and 590000 microseconds