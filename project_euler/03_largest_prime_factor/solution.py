NUM = 600851475143
SQRT = int(NUM**0.5)  # 775146


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False

    return True


prime_divisors = [i for i in range(2, SQRT) if NUM % i == 0 and is_prime(i)]
output = max(prime_divisors)  # [71, 839, 1471, 6857]
print(output)  # 6857
