# https://www.codewars.com/kata/586d6cefbcc21eed7a001155/train/python
# Quase k

def longest_repetition(chars):
    count = 0
    counts = []
    letters = []
    before_letter = None
    i = 0
    
    if not chars.strip() == '':
        for letter in chars:
            i += 1
            if count == 0:
                before_letter = letter
                count += 1
                continue

            if letter == before_letter:
                count += 1
            else:
                counts.append(count)
                letters.append(before_letter)
                count = 0
                before_letter = letter
                count += 1

            if len(chars) == i:
                counts.append(count)
                letters.append(before_letter)


        longest_value = max(counts)
        counts = [str(x) for x in counts]
        counts = "".join(counts)
        index = counts.find(str(longest_value))
        
        return (letters[index], longest_value)
    
    return ('', 0)

print(longest_repetition('kkkaaaaaa///////uuu'))