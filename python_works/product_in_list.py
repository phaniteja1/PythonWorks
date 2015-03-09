__author__ = 'phaniteja'

# This function is to calculate the product of all the numbers in the list


def product(numbers):

    final_product = 1

    for num in numbers:
        final_product = final_product * num

    return final_product

numbers_list = [2, 5, 10]

print_product = product(numbers_list)

print(print_product)
