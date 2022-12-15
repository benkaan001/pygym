# time module to calculate the total time the solution takes
import time 

# start time
start = time.time()

nums = []

for i in range(2,101):
    for j in range(2,101):
        num = i**j
        if num not in nums:
            nums.append(num)

print(nums)
print(len(nums)) #9183 

# end time
end = time.time()

print(f"Solution took {end - start} second(s)")
# Solution took 0.7711269855499268 second(s)