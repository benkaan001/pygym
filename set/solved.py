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
