RANGE_VALUE = 2000000

def is_prime(num):
    
    for i in range(2,num):
        if num % i == 0:
            return False 
        
    return True 

# create a generator object that will lazily evaluate the prime numbers
primes = (i for i in range(RANGE_VALUE +1) if is_prime(i))

print(primes) # <generator object <genexpr> at 0x108c05270>

# print the sum
# try:
#     total = sum(primes)
#     print(total) # 142913828922
# except Exception as e:
#     print(e)


