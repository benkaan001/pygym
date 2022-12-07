from factorial import factorial

digits = [int(i) for i in str(factorial(100))]
total = sum(digits)
print(total)  # 648
