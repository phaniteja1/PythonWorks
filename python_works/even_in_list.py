__author__ = 'phaniteja'

# This program is to find the even numbers in a list and put it in another list

new_numbers = []


def purify(numbers):

    for num in numbers:
        if num % 2 == 0:
            new_numbers.append(num)

    return new_numbers

numbers_list = [1, 2, 3, 4, 5, 6, 7]

print_list = purify(numbers_list)
print(print_list)
