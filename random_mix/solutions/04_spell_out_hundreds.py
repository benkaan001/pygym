
""" 
    Now include any number below 1000. 
        - Make sure to include 'and' in the spelling. 
        - Incorporate exception logic for various scenarios: ValueError etc
     
     Sample Input: 220
     Sample Output: "two hundred and twenty"
     
     Sample Input: 0
     Sample Output: 'zero
     
     Sample Input: 'hello' or '-1' or '29.9'
     Sample Output: 'some error message'
    
     
    
    
"""

D = {
    90: 'ninety',
    80: 'eighty',
    70: 'seventy',
    60: 'sixty',
    50: 'fifty',
    40: 'forty',
    30: 'thirty',
    20: 'twenty',
    19: 'nineteen',
    18: 'eighteen',
    17: 'seventeen',
    16: 'sixteen',
    15: 'fifteen',
    14: 'fourteen',
    13: 'thirteen',
    12: 'twelve',
    11: 'eleven',
    10: 'ten',
    9: 'nine',
    8: 'eight',
    7: 'seven',
    6: 'six',
    5: 'five',
    4: 'four',
    3: 'three',
    2: 'two',
    1: 'one',
}

def tens(num):
    if num in D:
        yield D[num]
    else:
        times, num = divmod(num, 10) # (2, 5)
        yield D[times*10]+' '+D[num] # D[20]= twenty d[5] = five
    

def hundreds(num):

    times, num = divmod(num, 100) # (2, 25)
    if times:
        yield D[times] # D[2] = two
        yield 'hundred'
    
    if num:
        if times:
            yield 'and'
        yield from tens(num) # twenty five 
        
# for i in hundreds(225):
#     print(i)
#
# """
# i = 'two'    | i = 'hundred'    | i = 'and'    | i = 'twenty five' 
# print('two') | print('hundred') | print('and') | print('twenty five') 
# """
    
def print_spell(num):
    
    try:
        if num < 0 or type(num) != int:
            raise Exception
    except Exception:
        print(f"Please enter a valid number between 0 and 999. Entered: {num}")
        return
        
    
    words = []
    
    if num:
        words += hundreds(num) # words = ['two', 'hundred', 'and', 'twenty five']
    else:
        words.append('zero')
    
    return print(" ".join(words))

print_spell(225)
print_spell(-225) # Please enter a valid number between 0 and 999. Entered: -225
print_spell('hello') # Please enter a valid number between 0 and 999. Entered: hello
print_spell(225.9) # Please enter a valid number between 0 and 999. Entered: 225.9

    