def is_palindrome(num):
    """ Accepts an integer and compares its iterable string version if it is a palindrome"""
    num = str(num)
    return num == num[::-1]

nums = []

# initiate two generators with range from mim 3-digit number to max 3-digit number
range1 = range(100, 999)
range2 = range(100, 999)

# iterate through both generators
for index, num in enumerate(range1):
    multiplication = num * range2[index]
    if is_palindrome(multiplication):
        nums.append(multiplication)

print(nums) # [10201, 12321, 14641, 40804, 44944, 69696, 94249, 698896]

# find the highest value in the nums iterable
max_num = max(nums)
print(max_num) # 698896