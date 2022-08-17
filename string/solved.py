# (1) Write a program to create a new string made of an input string’s first, middle, and last character.
from curses.ascii import isalpha, isdigit


str1 = "festive" # fte

new_str = str1[0] + str1[len(str1) // 2] + str1[len(str1)-1]
print(new_str)

# (2) Write a program to create a new string made of the middle three characters of an input string.
str1 = "JaSonAy" # Son
str1 = "JohonDipPeta" # Dip

mi = len(str1) // 2
output = str1[mi-1:mi+2]


# (3) Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.
s1 = "Aunt"
s2 = "Kelly" # AuKellynt

middle = len(s1) // 2
new_str = s1[:middle] + s2 + s1[middle:]
print(new_str)


# (4) Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and last characters.
s1 = "America"
s2 = "Japan" # AJrpan

transformed = s1[0] + s2[0] + s1[len(s1) // 2] + s2[len(s2) // 2] + s1[len(s1)-1] + s2[len(s2) -1]
print(transformed)


# (5) Write a program to arrange the characters of a string so that all lowercase letters should come first.

str1 = "PyNaTive" # yaivePNT

lower = []
upper = []

for i in str1:
   if i.islower():
    lower.append(i)
   else:
     upper.append(i)

joined = "".join(lower+upper)
print(joined)


# (6) Count all letters, digits, and special symbols from a given string
# Characters=8  Digits=3    Symbols=4

str1 = "P@#yn26at^&i5ve"

# can simply initalize count instead
char = []
digit = []
symbol = []

for i in str1:
    if i.isalpha():
        char.append(i)
    elif i.isdigit():
        digit.append(i)
    else:
        symbol.append(i)

print(f"Characters={len(char)}\nDigits={len(digit)}\nSymbols={len(symbol)}")


# (7) Given two strings, s1 and s2. Write a program to create a new string s3
# made of the first char of s1, then the last char of s2,
# Next, the second char of s1 and second last char of s2, and so on.
# Any leftover chars go at the end of the result.

s1 = "Abc"
s2 = "Xyz"  # AzbycX


joined = "".join( (s1[i] + s2[len(s2)-1-i]) for i in range(len(s1)))
print(joined)

# (8) Write a program to check if two strings are balanced.
# For example, strings s1 and s2 are balanced if all the characters in the s1 are present in s2.
# The character’s position doesn’t matter.

s1 = "Yn"
s2 = "PYnative"  # True

s1 = "Ynf"
s2 = "PYnative" # False

if s1 in s2: print(True)
else: print(False)



# (9) Write a program to find all occurrences of “USA” in a given string ignoring the case.

str1 = "Welcome to USA. usa awesome, isn't it?" # count = 2

count = str1.upper().count("USA")

print(count)


#


