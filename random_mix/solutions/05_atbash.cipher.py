from string import ascii_lowercase as lowercase_letters

cipher_letters = lowercase_letters[::-1]

print(lowercase_letters)  # abcdefghijklmnopqrstuvwxyz
print(cipher_letters)  # zyxwvutsrqponmlkjihgfedcba


def cipher(word):
    output = []
    for char in word:
        position = lowercase_letters.index(char)
        output.append(cipher_letters[position])
    return "".join(char for char in output)


word = "python"
print(cipher(word))

# one liner version
cypher2 = "".join(cipher_letters[lowercase_letters.index(char)] for char in word)
print(cypher2)
