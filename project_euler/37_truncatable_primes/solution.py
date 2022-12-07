def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


# Test
# print(is_prime(101))  # True
# print(is_prime(300))  # False


def is_truncatable_from_left(num):
    num = str(num)
    for index, _ in enumerate(num):
        temp = int(num[index:])
        if is_prime(temp):
            continue
        else:
            return False
    return True


# Test
# print(is_truncatable_from_left(37))  # True
# print(is_truncatable_from_left(30))  # False


def is_trunacatable_from_right(num):
    num = str(num)
    for index, _ in enumerate(num):
        temp = int(num[: len(num) - index])
        if is_prime(temp):
            continue
        else:
            return False
    return True


# Test
# print(is_trunacatable_from_right(37))  # True
# print(is_trunacatable_from_right(30))  # False

nums = [
    i
    for i in range(11, 1000000)
    if is_trunacatable_from_right(i) and is_truncatable_from_left(i)
]

print(nums)  # [23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397]
