# (1) Write a Python program to convert them into a dictionary in a way
# that item from list1 is the key and item from list2 is the value
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

list_to_dict = {key: value for key, value in zip(keys, values)}
print(list_to_dict)


# (2) Merge two Python dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

combined = {**dict1, **dict2}
print(combined)


# (3) Print the value of key ‘history’ from the below dict
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

print(sampleDict['class']['student']['marks']['history'])


# (4)  Initialize dictionary with default values
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
# {'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}

new_dict = dict.fromkeys(employees, defaults)
print(new_dict)


# (5) Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

keys = ["name", "salary"]
# {'name': 'Kelly', 'salary': 8000}

pythonic_dict = {key: sample_dict[key] for key in keys}
print(pythonic_dict)

# or
less_pythonic_dict = dict()
for key in keys:
    less_pythonic_dict.update({key: sample_dict[key]})
print(less_pythonic_dict)

# another one
new_dict = {}
for key in keys:
    if not key in sample_dict.items():
        new_dict[key] = sample_dict[key]
print(new_dict)


# (6) Delete a list of keys from a dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]
# {'city': 'New york', 'age': 25}

removed_item_values = [sample_dict.pop(key) for key in keys]
print(sample_dict)
print(removed_item_values)  # ['Kelly', 8000]


# another comprehension
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
sample_dict = {key: sample_dict[key] for key in sample_dict.keys() - keys}
print(sample_dict)


# (7) Write a Python program to check if value 200 exists in the following dictionary.
sample_dict = {'a': 100, 'b': 200, 'c': 300}
# 200 present in a dict

print('200 is present') if 200 in sample_dict.values(
) else print('200 is not there')
