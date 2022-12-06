from names import name_list

# test 
print(name_list[2]) # LINDA

# instead of manually creating the dictionary, iterate through letters string
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
value_dict = {}


# initiate the beginning index value to 1 instead of default 0
for index,letter in enumerate(letters, start=1):
    value_dict[letter] = index 

print(value_dict)
"""
{'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 
 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 
 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 
 'Z': 26}
"""

def calculate_value(name):
    """Accepts a name and returns the total value of letters based on values listed in value_dict"""
    total = 0
    letters = [char for char in name]
    for key,value in value_dict.items():
        if key in letters:
            total += value 
    return total 

values = [ calculate_value(name) for name in name_list ]

values_total = sum(values) # 291286

position_values_total = sum(range(len(name_list))) # 13325703

final_sum = values_total + position_values_total # 13616989
