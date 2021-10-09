# https://www.codewars.com/kata/52b7ed099cdc285c300001cd/train/python
# SUCCESS

def sum_of_intervals(intervals):

    count_intervals = 0
    list_numbers = []

    for interval_item in intervals:
        interval_item = list(interval_item)
        while interval_item[0] != interval_item[1]:
            interval_item[0] += 1
            if not interval_item[0] in list_numbers:
                count_intervals += 1 
            list_numbers.append(interval_item[0])

    return count_intervals

print(sum_of_intervals([[1,4],[7, 10],[3, 5]]))
