# https://www.codewars.com/kata/51b66044bce5799a7f000003/train/python
# SUCCESS

class RomanNumerals:

    def to_roman(val):
        symbols = ''
        num = [1, 4, 5, 9, 10, 40, 50, 90,
        100, 400, 500, 900, 1000]
        sym = ["I", "IV", "V", "IX", "X", "XL",
            "L", "XC", "C", "CD", "D", "CM", "M"]
        i = 12

        while val:
            div = val // num[i] # Vai ver quantas vezes ele precisa desse numero
            val %= num[i] # Tirar o numero

            while div:
                symbols += sym[i]
                div -= 1
            i -= 1

        return symbols

    def from_roman(roman_num):
        symbols = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        count = 0
        previous_value = 0
        for num in roman_num:
            actual_value = symbols[num]

            if previous_value == 0:
                previous_value = actual_value

            if previous_value < actual_value:
                count += actual_value - (previous_value * 2)
                previous_value = actual_value
            else:
                count += actual_value
                previous_value = actual_value


print(RomanNumerals.from_roman('MMMDXLIX'))
print(RomanNumerals.to_roman(123456))