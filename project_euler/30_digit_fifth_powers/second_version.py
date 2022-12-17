

# Given a list of numbers print if each number can be written as the sum of fourth powers of their digits
numbers = [1634, 8208, 9474]


numbers = [str(i) for i in numbers] # ['1634', '8208', '9474'] 


# descriptive version
num_list = []
for number in numbers:
    digits = [i for i in number]
    num_list.append(digits)
    
#  num_list = [['1', '6', '3', '4'], ['8', '2', '0', '8'], ['9', '4', '7', '4']]


# one liner version
number_list = [[i for i in number] for number in numbers]
# [['1', '6', '3', '4'], ['8', '2', '0', '8'], ['9', '4', '7', '4']]

sums = []
for l in number_list:
    sum =0
    for num in l:
        sum+= int(num)**4
    sums.append(sum)
        
# sums = [1634, 8208, 9474] 

# compare if all numbers in sums list are also present in the original numbers list
output = all(i for i in numbers if i in sums) # True 



