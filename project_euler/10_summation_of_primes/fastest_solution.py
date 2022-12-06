
def sum_primes(num):
    
    sum = 0
    sieve = [True] * num
    
    for p in range(2, num):
        if sieve[p]:
            sum += p 
            for i in range(p*p, num, p):
                sieve[i] = False 
    
    return sum 

print(sum_primes(2000000)) # 142913828922
    