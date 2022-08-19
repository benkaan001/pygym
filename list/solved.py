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
