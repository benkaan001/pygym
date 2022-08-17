# (1) Write a program to create a new string made of an input string’s first, middle, and last character.
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
s2 = "Kelly" #AuKellynt

middle = len(s1) // 2
new_str = s1[:middle] + s2 + s1[middle:]

# (4) Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and last characters.
s1 = "America"
s2 = "Japan" #AJrpan

