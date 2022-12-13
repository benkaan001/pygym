from number import number_string

number_string = number_string.replace("\n", "")

numbers = []

while len(number_string) > 50:
    num = 0
    temp = number_string[num : 51 + num]
    numbers.append(int(temp))
    num += 50
    number_string = number_string[num:]

# on a single line
first_ten = str(sum(int(str(num)[:11]) for num in numbers))[:11]
print(first_ten)  # 54838726961

# detailed
ten_digit_numbers = [int(str(num)[:11]) for num in numbers]
ten_digit_sum = sum(ten_digit_numbers)
first_ten = str(ten_digit_sum)[:11]
print(first_ten)  # 54838726961
