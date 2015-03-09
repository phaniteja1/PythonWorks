__author__ = 'phaniteja'

# This program is to find the median in a list


def find_median(numbers):

    numbers.sort()
    if len(numbers) % 2 != 0:
        median = numbers[(len(numbers)-1) // 2]

    else:
        median = (numbers[(len(numbers) // 2) - 1] + numbers[(len(numbers) // 2)]) / 2
    return median

numbers_list = [3, 7, 4, 5, 6, 8]

print_median = find_median(numbers_list)

print(print_median)