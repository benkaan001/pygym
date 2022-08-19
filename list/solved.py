# (1) Reverse the given list
list1 = [100, 200, 300, 400, 500]  # [500, 400, 300, 200, 100]

# using built-in reverse
list1.reverse()
print(list1)

# more pythonic
list1 = [100, 200, 300, 400, 500]
list1 = list1[::-1]
print(list1)

# (2) Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list,
# then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.
list1 = ["H", "na", "i", "Ke"]
list2 = ["er", "me", "s", "lly"]
# ['Her', 'name', 'is', 'Kelly']

new_list = [i + j for i, j in zip(list1, list2)]
print(new_list)

# less pythonic
new_list = []
for i in range(len(list1)):
    new_list.append("".join(list1[i]+list2[i]))
print(new_list)


# (3) Given a list of numbers. write a program to turn every item of a list into its square.
numbers = [1, 2, 3, 4, 5, 6, 7]  # [1, 4, 9, 16, 25, 36, 49]

squared = [num**2 for num in numbers]
print(squared)


# (4) Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

nested_list = [i + y for i in list1 for y in list2]
print(nested_list)


# (5) Given a two Python list. Write a program to iterate both lists simultaneously
# and display items from list1 in original order and items from list2 in reverse order.
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]  # 10 400   20 300   30 200   40 100

for x, y in zip(list1, list2[::-1]):
    print(x, y)


# (6) Remove empty strings from the list of strings
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# ['Mike', 'Emma', 'Kelly', 'Brad']

filtered_list = list(filter(None, list1))
print(filtered_list)

# more Pythonic
filtered_list = [i for i in list1 if bool(i) == True]
print(filtered_list)


# (7) Write a program to add item 7000 after 6000 in the following Python List
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]

list1[2][2].append(7000)
print(list1)

# using insert
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].insert(2, 7000)
print(list1)
