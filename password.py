from itertools import chain, product
import string

# https://stackoverflow.com/questions/11747254/python-brute-force-algorithm
# generate password combinations
def bruteforce(charset, maxlength):
    return (''.join(candidate)for candidate in chain.from_iterable(product(charset, repeat=i)for i in range(1, maxlength + 1)))


print(bruteforce(string.ascii_lowercase, 2))

