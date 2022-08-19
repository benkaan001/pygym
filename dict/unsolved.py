# (1) Write a Python program to convert them into a dictionary in a way
# that item from list1 is the key and item from list2 is the value
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}


# (2) Merge two Python dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}


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


# (4)  Initialize dictionary with default values
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
# {'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}
# HINT explore built-in dict methods


# (5) Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

keys = ["name", "salary"]
# {'name': 'Kelly', 'salary': 8000}


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


# (7) Write a Python program to check if value 200 exists in the following dictionary.
sample_dict = {'a': 100, 'b': 200, 'c': 300}
# 200 present in a dict


# (8) Write a program to rename a key city to a location in the following dictionary.
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
# {'name': 'Kelly', 'age': 25, 'salary': 8000, 'location': 'New york'}


# (9) Get the key of a minimum value from the following dictionary
sample_dict = {
    'Physics': 82,
    'Math': 65,
    'history': 75
}
# Math


# (10) Change value of a key in a nested dictionary
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}
# 'emp3': {'name': 'Brad', 'salary': 8500}
