def factorial(num):
    sum = 1

    for _ in range(num):
        sum *= num
        num -= 1
        if num <= 1:
            break

    return sum


# print(factorial(5)) # 120


# def factorial(num):
#     total = 1

#     if num <= 1:
#         return 1
#     else:
#         for i in range(2, num + 1):
#             total *= i

#     return total


# print(factorial(5)) # 120


# def factorial(num):
#     if num <= 1:
#         return 1
#     else:
#         return factorial(num - 1) * num

# print(factorial(5))
