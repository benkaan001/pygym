total = str(sum(i**i for i in range(1, 1001)))
last_ten_digits = total[len(total) - 10 :]
print(last_ten_digits)  # 9110846700
