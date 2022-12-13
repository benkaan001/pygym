def get_substrings(s, n):
    out = []
    
    while len(s) >= n:
        num = 0
        temp = s[num:n+num]
        out.append(int(temp))
        s = s[num+1:]
    
    return out


s = "512775"
n = 3
print(get_substrings(s, n))


"""
num = 0      | num = 0          | num = 0               | num = 0 
temp = '512' | temp = '127'     | temp = '277'          | temp = '775' 
out = [512]  | out = [512, 127] | out = [512, 127, 277] | out = [512, 127, 277, 775] 
s = '12775'  | s = '2775'       | s = '775'             | s = '75' 

return [512, 127, 277, 775] 


"""

n = 4
print(get_substrings(s, n)) # [5127, 1277, 2775]