import secrets


secrets_generator = secrets.SystemRandom()

password = secrets_generator.randrange(100000, 999999)

print(f"Your one time password is: {password}")
