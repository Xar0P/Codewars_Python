# https://www.codewars.com/kata/51ba717bb08c1cd60f00002f/train/python
# SUCCESS

def solution(args):
    def verify(range_extraction, count):
        if not range_extraction == None and count > 1:
            solved.append(f'{actual}-{args[i]}')
            range_extraction = None
            count = 0
        elif count == 1:
            solved.append(f'{actual}')
            solved.append(f'{args[i]}')
            count = 0
        else:
            solved.append(f'{actual}')

    solved = []
    extraction = True
    range_extraction = None
    count = 0

    for i in range(0, len(args)):
        if extraction:
            actual = args[i]

        if not i + 1 == len(args):
            if args[i] + 1 == args[i + 1] or args[i] - 1 == args[i + 1]:
                extraction = False
                range_extraction = args[i]
                count += 1
            else:
                extraction = True
                verify(range_extraction, count)
        else:
            verify(range_extraction, count)

    return ",".join(solved)

print(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]))