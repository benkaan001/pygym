import random

""" (1) Generate 3 random integers between 100 and 999 which is divisible by 5 """


print("Three random numbers divisible by 5 are : ")
for num in range(3):
    print(random.randrange(100, 999, 5), end=", ")
