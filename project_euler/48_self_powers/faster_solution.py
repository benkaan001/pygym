MOD = 10**10
total = sum(i**i for i in range(1, 1001))
last_ten_digits = total % MOD
print(last_ten_digits)  # 9110846700
