import random
import time


def generate_random_date(start_date, end_date):
    """ Generates a random date between given start date and end date"""

    print(f"Printing a random date between {start_date} and {end_date}")
    random_generator = random.random()
    date_format = "%m/%d/%Y"

    start_time = time.mktime(time.strptime(start_date, date_format))
    end_time = time.mktime(time.strptime(end_date, date_format))
    # print(start_time, end_time)  # 1661317200.0 2524629600.0

    random_time = start_time + random_generator * (end_time - start_time)
    # print(random_time)  # 2166547546.169486
    random_date = time.strftime(date_format, time.localtime(random_time))

    return random_date


random_date = generate_random_date("08/24/2022", "01/01/2050")
print("Random date: ", random_date)

# Printing a random date between 08/24/2022 and 01/01/2050
# Random date:  04/17/2043
