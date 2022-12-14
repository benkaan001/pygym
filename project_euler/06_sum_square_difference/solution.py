TARGET = 100 

sum_sqr = sum(i**2 for i in range(TARGET+1)) # 338350
sqr_sum = sum(i for i in range(TARGET+1))**2 # 25502500

diff = sqr_sum - sum_sqr # 25164150 
