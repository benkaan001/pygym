# Determine if a given word is an isogram.
# An isogram/non-pattern word is a word without repeating letters.
words = ["lumberjacks", "isograms", "downstream", "happy", "extra"]

# comprehension
output = [True if len(i) == len(set(i)) else False for i in words]
print(output)  # [True, False, True, False, True]


# more detailed
def is_isogram(word):
    return len(word) == len(set(word))


out_list = []
for word in words:
    output = True if is_isogram(word) else False
    out_list.append(output)

print(out_list)  # # [True, False, True, False, True]
