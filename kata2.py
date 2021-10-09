# https://www.codewars.com/kata/517abf86da9663f1d2000003/train/python
# SUCESS

def to_camel_case(text):
    if text == '':
        return ''

    if '-' in text or '_' in text:
        text = text.split('-')
        for i in range(0,len(text)):
            if '_' in text[i]:
                text[i] = text[i].split('_')
                for j in range(0,len(text[i])):
                    if text[i][j] == text[0][0]:
                        text[i][j] = text[i][j]
                    else:
                        text[i][j] = text[i][j].title()
                    
                text[i] = ''.join(text[i])
            else:
                if text[i] == text[0]:
                    text[i] = text[i]
                else:
                    text[i] = text[i].title()
        
        return ''.join(text)

print(to_camel_case('to_camel_case'))