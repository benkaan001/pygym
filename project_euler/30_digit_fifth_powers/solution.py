

output = 0

# experimental upper limit - add x10 and continue  
UPPER_LIMIT = 10*(10**5)

for i in range(2, UPPER_LIMIT):
    
    str_i = [x for x in str(i)]
    
    fifth_power_i = [int(x)**5 for x in str_i]
    
    fifth_power_sum = sum(fifth_power_i)

    if fifth_power_sum == i:
        output += i

#printing the solution
print (output) # 443839

