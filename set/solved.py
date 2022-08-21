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


# (5) Write a Python program to remove items 10, 20, 30 from the following set at once.
set1 = {10, 20, 30, 40, 50}
# {40,50}

set1 = {item for item in set1 if item >= 40}
print(set1)

# built-in difference_update takes in an iterable
set1 = {10, 20, 30, 40, 50}
set1.difference_update([10, 20, 30])
print(set1)


# (6)  Return a set of elements present in Set A or B, but not both
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
# {20, 70, 10, 60}

# built-in symetric difference
print(set1.symmetric_difference(set2))

# super unncessary solution
unique_set1 = {item for item in set1 if item not in set2}
unique_set2 = {item for item in set2 if item not in set1}
print(set(list(unique_set1)+list(unique_set2)))


# (7) Check if two sets have any elements in common. If yes, display the common elements
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
# {10}

if set1.isdisjoint(set2):
    print("No items in common")
else:
    print(f"Common items are: {set1.intersection(set2)}")


# (8) Update set1 by adding items from set2, except common items
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
# {70, 10, 20, 60}


# (9) Remove items from set1 that are not common to both set1 and set2
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
# {40, 50, 30}
