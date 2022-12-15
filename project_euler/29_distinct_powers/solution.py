

nums = []

for i in range(2,101):
    for j in range(2,101):
        num = i**j
        if num not in nums:
            nums.append(num)

print(len(nums)) #9183 
