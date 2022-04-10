import random
# given a list of numbers
numbers = [5, 4, 8, 23, 25, 56, 7, 9, 2, 14, 18, 10]

# add the random number to the list, hint numbers.append
random_number = random.randint(0, 100)
numbers.append(random_number)
print(numbers)

# find the largest number
largest_number = 0
for number in numbers:
    if number > largest_number:
        largest_number = number

print(f'The largest number is: {largest_number}')

# find the smallest number
smallest_number = numbers[0]
for number in numbers:
    if number < smallest_number:
        smallest_number = number

print(f'The smallest non-zero number is: {smallest_number}')


# create 2 functions based on the above

