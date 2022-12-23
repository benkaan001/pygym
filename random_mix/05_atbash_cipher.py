"""
Given a string, return the atbash cipher version of the string.

Example Input -> python
Expected Output -> kbgslm

"""

from string import ascii_lowercase as lowercase_letters

cipher_letters = lowercase_letters[::-1]

print(lowercase_letters)  # abcdefghijklmnopqrstuvwxyz
print(cipher_letters)  # zyxwvutsrqponmlkjihgfedcba
