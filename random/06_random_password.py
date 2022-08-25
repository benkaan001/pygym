import random
import string

# choice() can repeat characters whereas sample() does not


def generate_password():
    """Generates a password that has 10 characters and minimum : 2 UPPERCASE, 1 digit, 1 special character"""
    random_source = string.ascii_letters + string.digits + string.punctuation
    password = random.sample(random_source, 6)
    password += random.sample(string.ascii_uppercase, 2)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)

    print(password)  # ['A', ')', '8', 'p', 'd', 'C', 'B', 'W', '7', '<']
    return "".join(password)


random_pass = generate_password()
print(random_pass)  # A)8pdCBW7<
