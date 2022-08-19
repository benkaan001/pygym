import string
import re


# (1) Write a program to create a new string made of an input string’s first, middle, and last character.
str1 = "festive"  # fte

new_str = str1[0] + str1[len(str1) // 2] + str1[len(str1)-1]
print(new_str)

# (2) Write a program to create a new string made of the middle three characters of an input string.
str1 = "JaSonAy"  # Son
str1 = "JohonDipPeta"  # Dip

mi = len(str1) // 2
output = str1[mi-1:mi+2]


# (3) Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.
s1 = "Aunt"
s2 = "Kelly"  # AuKellynt

middle = len(s1) // 2
new_str = s1[:middle] + s2 + s1[middle:]
print(new_str)


# (4) Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and last characters.
s1 = "America"
s2 = "Japan"  # AJrpan

transformed = s1[0] + s2[0] + s1[len(s1) // 2] + \
    s2[len(s2) // 2] + s1[len(s1)-1] + s2[len(s2) - 1]
print(transformed)


# (5) Write a program to arrange the characters of a string so that all lowercase letters should come first.
str1 = "PyNaTive"  # yaivePNT

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

joined = "".join((s1[i] + s2[len(s2)-1-i]) for i in range(len(s1)))
print(joined)

# (8) Write a program to check if two strings are balanced.
# For example, strings s1 and s2 are balanced if all the characters in the s1 are present in s2.
# The character’s position doesn’t matter.
s1 = "Yn"
s2 = "PYnative"  # True
s1 = "Ynf"
s2 = "PYnative"  # False

if s1 in s2:
    print(True)
else:
    print(False)


# (9) Write a program to find all occurrences of “USA” in a given string ignoring the case.
str1 = "Welcome to USA. usa awesome, isn't it?"  # count = 2

count = str1.upper().count("USA")
print(count)


# (10) Given a string s1, write a program to return the sum and average of the digits
# that appear in the string, ignoring all other characters.
str1 = "PYnative29@#8496"  # Sum is: 38 Average is  6.333333333333333

digits = [int(i) for i in str1 if i.isdigit()]  # [2, 9, 8, 4, 9, 6]

digits_sum = sum(digits)
digits_avg = digits_sum / len(digits)
print(f"Sum is: {digits_sum}\nAverage is: {digits_avg}")


# (11) Write a program to count occurrences of all characters within a string
str1 = "Apple"  # {'A': 1, 'p': 2, 'l': 1, 'e': 1}

str_dic = {letter: str1.count(letter) for letter in str1}
print(str_dic)


# (12) Reverse a given string
str1 = "PYnative"   # evitanYP

str1_reversed = "".join(sorted(str1, reverse=True))
str1_reversed = str1[::-1]
print(str1_reversed)

# most cost effective
str1 = "".join(reversed(str1))
print(str1)


# (13) Write a program to find the last position of a substring “Emma” in a given string.
str1 = "Emma is a data scientist who knows Python. Emma works at google."
# Last occurrence of Emma starts at index 43

index = str1.rfind("Emma")
print(f"Last occurrence of Emma starts at index {index}")


# (14) Split a string on hyphens
str1 = "Emma-is-a-data-scientist"  # Emmaisadatascientist
print("".join(str1.split("-")))


# (15)  Remove empty strings from a list of strings
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
# ['Emma', 'Jon', 'Kelly', 'Eric']

sorted_str = [i for i in str_list if i]
print(sorted_str)
filtered = list(filter(None, str_list))
print(filtered)
booled = list(filter(lambda x: bool(x) == True, str_list))
print(booled)


# (16) Remove special symbols / punctuation from a string
str1 = "/*Jon is @develo^^^per & musician&&"     # "Jon is developer musician"

clean_str1 = re.sub(r'[^\w\s]', '', str1)
print(clean_str1)


# (17) Removal all characters from a string except integers
str1 = "She is 25 years and 10 months old"  # 2510

filtered = "".join(list(filter(lambda x: x.isdigit(), str1)))
print(filtered)
str1_comp = "".join([i for i in str1 if i.isdigit()])
print(str1_comp)


# (18) Write a program to find words with both alphabets and numbers from an input string.
str1 = "Emma25 is Data scientist50 and AI Expert"  # Emma25 , scientist50

alpha_numeric = [word for word in str1.split(
    " ") if any(char.isalpha() for char in word) and any(char.isdigit() for char in word)]
print(alpha_numeric)


# (19) Replace each special symbol with # in the following string
str1 = "/*Jon is @developer & musician!!"
# ##Jon is #developer # musician##

for char in string.punctuation:
    str1 = str1.replace(char, "#")
print(str1)
