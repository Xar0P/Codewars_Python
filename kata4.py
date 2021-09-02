# https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python
# SUCESS

def find_it(seq):
    numbers = {}
    
    for i in range(0,len(seq)):
        if seq[i] in numbers.keys():
            numbers[seq[i]] = numbers[seq[i]] + 1           
        else:
            numbers[seq[i]] = 1
        
    for key in numbers:
        if not numbers[key] % 2 == 0:
            return key

print(find_it([1,1,1,1,1,1,10,1,1,1,1]))