# (1) Reverse the given tuple
tuple1 = (10, 20, 30, 40, 50)
# (50, 40, 30, 20, 10)

tuple1_reversed = tuple1[::-1]
print(tuple1_reversed)

# reversed class returns an iterator that iterates over given squence
reversed_tuple = tuple(reversed(tuple1))
print(reversed_tuple)


# (2) The given tuple is a nested tuple. write a Python program to print the value 20.
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))

print(tuple1[1][1])


# (3) Create a tuple with single item 50

tuple1 = (30,)


# (4) Write a program to unpack the following tuple into four variables and display each variable.
tuple1 = (10, 20, 30, 40)  # a = 10, b = 20, c = 30 , d = 40

a, b, c, d = tuple1
print(f"a={a}, b={b}, c={c}, d={d}")


# (5) Swap given two tuples
tuple1 = (11, 22)       # tuple1 = (99,88)
tuple2 = (99, 88)       # tuple2 = (11,22)

tuple1, tuple2 = tuple2, tuple1
print(f"tuple1={tuple1}, tuple2={tuple2}")


# (6) Write a program to copy elements 44 and 55 from the following tuple into a new tuple.
tuple1 = (11, 22, 33, 44, 55, 66)  # tuple2: (44, 55)

tuple2 = tuple1[3:5]
tuple2 = tuple1[3:-1]
print(tuple2)


# (7) Write a program to modify the first item (22) of a list inside a following tuple to 222
tuple1 = (11, [22, 33], 44, 55)
# tuple1: (11, [222, 33], 44, 55)

tuple1[1][0] = 222
print(tuple1)


# (8) Sort a tuple of tuples by 2nd item
tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
# (('c', 11), ('a', 23), ('d', 29), ('b', 37))

sorted_tuple = tuple(sorted(tuple1, key=lambda x: x[1]))
print(sorted_tuple)


# (9) Counts the number of occurrences of item 50 from a tuple
tuple1 = (50, 10, 60, 70, 50)

print(tuple1.count(50))


# (10) Check if all items in the tuple are the same
tuple1 = (45, 45, 45, 45)

print(True) if len(tuple1) != len(set(tuple1)) else print(False)
