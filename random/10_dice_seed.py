import random


print("Seeded random numbers: ")
for i in range(5):
    random.seed(100)
    seeded_random = random.randrange(1, 7)
    print(seeded_random, end=" ")

print("\nRegular random numbers: ")
for i in range(5):
    not_seeded = random.randrange(1, 7)
    print(not_seeded, end=" ")

# Seeded random numbers:
# 2 2 2 2 2
# Regular random numbers:
# 4 4 2 6 4
