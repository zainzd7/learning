
# find the largest number
def find_largest_number(numbers):
    largest_number = 0
    for number in numbers:
        if number > largest_number:
            largest_number = number

    return largest_number


# find the smallest number
def find_smallest_number(numberz):
    smallest_number = numberz[0]
    for number in numberz:
        if number < smallest_number:
            smallest_number = number

    print(f'The smallest non-zero number is: {smallest_number}')
