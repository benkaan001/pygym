import random
import string

# random.choices(sequence, weights=None, cum_weights=None, k=1)
# The choices() method returns a list with the randomly selected element from the specified sequence.
# You can weigh the possibility of each result with the weights parameter or the cum_weights parameter.
# The sequence can be a string, a range, a list, a tuple or any other kind of sequence.


def generate_random_string(str_len):
    """Generates a random string of 5 characters"""
    letters = string.ascii_letters  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    # return "".join(random.choice(letters) for i in range(str_len))
    # print(random.choices(letters, k=5))  # ['Y', 'x', 'v', 'H', 'd']
    return "".join(random.choices(letters, k=5))  # kwOur


rand_str1 = generate_random_string(5)
print(rand_str1)
