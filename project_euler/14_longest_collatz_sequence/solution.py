def collatz(number):
    numbers = []

    while number > 1:
        num = number
        temp = num / 2 if num % 2 == 0 else (3 * num) + 1
        numbers.append(int(temp))
        number = temp

    return numbers


number = 13
print(collatz(number))  # [40, 20, 10, 5, 16, 8, 4, 2, 1]


lengths = {}
for i in range(1000000, 0, -1):
    l = len(collatz(i))
    lengths[l] = i

result = {key: value for key, value in lengths.items() if key == max(lengths.keys())}
print(result)  # {524: 837799}

print(result.items())  # dict_items([(524, 837799)])
((chain_length, chain_number),) = result.items()
print(chain_number)  # 8377799
