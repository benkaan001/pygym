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
