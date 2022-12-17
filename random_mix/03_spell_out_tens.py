
""" 
     Write a program that take a number between 0 and 100 exclusive
     and spell out that number in English.
     
     Sample Input: 99
     Sample Output: "ninety nine"
     
    
    
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

print(divmod(100, 3)) # (33,1)

def tens(num):
    if num in D:
        yield D[num]
    else:
        times, num = divmod(num, 10)
        yield D[times*10]+' '+D[num]

print(tens(99)) # <generator object tens at 0x10e41e0b0>
    
words = [word for word in tens(99)]    # words = ['ninety nine'] 
print(" ".join(words)) # ninety nine 
    


    
    
