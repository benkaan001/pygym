import random


first_float = random.uniform(0.1, 1.0)
second_float = random.uniform(9.5, 99.5)
result = round(first_float * second_float, 3)

print(
    f" Rounded result by 3 decimal points: {first_float} x {second_float} = {result} ")
#  Rounded result by 3 decimal points: 0.8048358333796208 x 97.73827283251121 = 78.663
