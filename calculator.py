# https://www.codewars.com/kata/5235c913397cbf2508000048/train/python
# SUCCESS

class Calculator(object):
    def evaluate(self, string: str):
        equation = string.split(' ')
        i = 0

        while '(' in equation:
            eq_reversed = equation[::-1].index('(')
            j = -equation[::-1].index('(')

            while equation[j] != equation[equation.index(')')]:
                if equation[j] == '/':
                    calc = float(equation[j - 1]) / float(equation[j + 1])
                    equation[j] = calc
                    equation.pop(j - 1)
                    equation.pop(j + 1)
                    j = -eq_reversed
                elif equation[j] == '*':
                    calc = float(equation[j - 1]) * float(equation[j + 1])
                    equation[j] = calc
                    equation.pop(j - 1)
                    equation.pop(j + 1)
                    j = -eq_reversed
                j += 1

            j = -eq_reversed

            while equation[j] != equation[equation.index(')')]:
                if equation[j] == '+':
                    calc = float(equation[j - 1]) + float(equation[j + 1])
                    equation[j] = calc
                    equation.pop(j - 1)
                    equation.pop(j + 1)
                    j = -eq_reversed
                elif equation[j] == '-':
                    calc = float(equation[j - 1]) - float(equation[j + 1])
                    equation[j] = calc
                    equation.pop(j - 1)
                    equation.pop(j + 1)
                    j = -eq_reversed
                j += 1

            equation.pop(-equation[::-1].index('(') - 1)
            equation.pop(equation.index(')'))
            continue

        i = 0
        while i != len(equation):
            if equation[i] == '/':
                calc = float(equation[i - 1]) / float(equation[i + 1])
                equation[i] = calc
                equation.pop(i - 1)
                equation.pop(i)
                i = 0
            elif equation[i] == '*':
                calc = float(equation[i - 1]) * float(equation[i + 1])
                equation[i] = calc
                equation.pop(i - 1)
                equation.pop(i)
                i = 0
            i += 1

        i = 0

        while i != len(equation):
            if equation[i] == '+':
                calc = float(equation[i - 1]) + float(equation[i + 1])
                equation[i] = calc
                equation.pop(i - 1)
                equation.pop(i)
                i = 0
            elif equation[i] == '-':
                calc = float(equation[i - 1]) - float(equation[i + 1])
                equation[i] = calc
                equation.pop(i - 1)
                equation.pop(i)
                i = 0
            i += 1

        equation[0] = str(equation[0])
        return float("".join(equation))

print(Calculator().evaluate("2 * ( 2 * ( 2 * ( 2 * 1 ) ) )"))
# 2 + 3 * 4 / 3 - 6 / 3 * 3 + 8