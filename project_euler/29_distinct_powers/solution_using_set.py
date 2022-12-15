# time module to calculate the total time the solution takes
import time 

# import the difference from the second solution
from solution import diff1

# start time
start = time.time()

nums = [ i**j for j in range(2,101) for i in range(2,101)]

print(len(set(nums))) 

# end time
end = time.time()

diff2 = end - start

print(f"Took {diff2} second(s), {diff1 // diff2} times faster! ")

# Took 0.005304098129272461 second(s), 132.0 times faster! 
