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

# 1) calculate the timedifference
 
print('timediff = 0:11:46.590000') 

# 2) unpack hour, minute, second from timediff
print(" hour = 0, minute = 11, second = 46.590000") 

# 3) print time diff including microseconds
print("Time difference between object1 and object2 are 0 hour(s), 11 minute(s), 46 second(s), and 590000 microseconds")