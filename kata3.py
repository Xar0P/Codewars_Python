# https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python
# SUCESS

import re

def pig_it(text):
    new = []
    
    text = text.split()
    
    for i in range(0,len(text)):
        for j in range(0, len(text[i])):
            if not j == 0:
                new.append(text[i][j])
                   
            x = re.search('[A-Za-z]',text[i][j])
            
            if x:
                if i + 1 == len(text) and j + 1 == len(text[i]):
                    new.append(f'{text[i][0]}ay')
                elif j + 1 == len(text[i]):
                    new.append(f'{text[i][0]}ay ')
            else:
                if i + 1 == len(text) and j + 1 == len(text[i]):
                    new.append(f'{text[i][0]}')
                elif j + 1 == len(text[i]):
                    new.append(f'{text[i][0]} ')
                
    return ''.join(new)

print(pig_it('Pig latin is cool'))