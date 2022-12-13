from number import number_string

# challenge calculate the sum of first 10 digits of each of the 50-digit number


def pretify(s):
    """Returns a list of 50-digit strings from a given string"""

    nums = []

    while len(s) > 50:
        num = 0
        temp = s[num : num + 51]
        temp = temp.replace("\n", "")  # remove the tab
        nums.append(temp)
        num += 50
        s = s[num:]

    has_defect = any(i for i in nums if len(i) != 50)  # False

    defected_nums = {nums.index(i): i for i in nums if len(i) != 50}  # {}

    result = nums if not has_defect else defected_nums

    return result


nums = pretify(number_string)

# one liner
total = 0
total += sum(int(i) for num in nums for i in num[:11])
print(total)  # 5188


# detailed
total = 0
for num in nums:
    num_total = sum(int(i) for i in num[:11])
    total += num_total

print(total)  # 5188
