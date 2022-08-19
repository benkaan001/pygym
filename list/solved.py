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


# (8) You have given a nested list. Write a program to extend it by adding the sublist
# ["h", "i", "j"] in such a way that it will look like the following list.
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]
# ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']

list1[2][1][2].extend(sub_list)
print(list1)


# (9) Write a program to find value 20 in the list, and if it is present,
# replace it with 200. Only update the first occurrence of an item.
list1 = [5, 10, 15, 20, 25, 50, 20]
# [5, 10, 15, 200, 25, 50, 20]

index = list1.index(20)
list1[index] = 200
print(list1)


# using built-in remove and insert
list1 = [5, 10, 15, 20, 25, 50, 20]
index = list1.index(20)
list1.remove(list1[index])
list1.insert(index, 200)
print(list1)


# (10) Given a Python list, write a program to remove all occurrences of item 20.
list1 = [5, 20, 15, 20, 25, 50, 20]
# [5, 15, 25, 50]

list1 = [num for num in list1 if num != 20]
print(list1)
