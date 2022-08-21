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
