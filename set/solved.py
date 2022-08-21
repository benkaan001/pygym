# (1) Write a program to add all its elements into a given set.
sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]
# {'Green', 'Yellow', 'Black', 'Orange', 'Red', 'Blue'}

# update takes an iterable
sample_set.update(sample_list)
print(sample_set)

# add takes an item
for item in sample_list:
    sample_set.add(item)
print(sample_set)


sample_set = {"Yellow", "Orange", "Black"}
sample_set.update(item.upper() for item in sample_list)
print(sample_set)  # {'RED', 'GREEN', 'BLUE', 'Black', 'Orange', 'Yellow'}


# (2) Return a new set of identical items from two sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
# {40, 50, 30}

union = set(set1 & set2)
print(union)

# using built-in intersection method
print(set1.intersection(set2))


# (3) Return a new set with unique items from both sets by removing duplicates.
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
# {70, 40, 10, 50, 20, 60, 30}

combined = set1.union(set2)
print(combined)


combined2 = set([*set1, *set2])
print(combined2)


# (4) Update the first set with items that don’t exist in the second set
set1 = {10, 20, 30}
set2 = {20, 40, 50}
# set1 {10, 30}

# method 1
set1 = set1 - set2
print(set1)  # {10, 30}

# using difference_update method
set1 = {10, 20, 30}
set2 = {20, 40, 50}
difference = set1.difference(set2)
print(difference)  # {10, 30}
print(set1)  # {10, 20, 30}

set1.difference_update(set2)
print(set1)  # {10, 30}
