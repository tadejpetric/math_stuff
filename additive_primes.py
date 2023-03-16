"""

"""
from functools import reduce

primer = [5,7,11] # the initial set of additive primes
limit = 1000 # display additive primes up to 100




def increment(primer, i):
    (x, y) = primer[i]
    primer[i] = (x, y+1)

def decrement(primer, i):
    (x, y) = primer[i]
    primer[i] = (x, min(0,y-1))

def carry(primer, i):
    increment(primer, i)
    while i > 0:
        i -= 1
        x, y = primer[i]
        primer[i] = (x, 0)


def compute(primer):
    return reduce(lambda x, y: x + y[0]*y[1], [0]+primer)

def display(primer, limit, sieve, occurances=False):
    print("Field for additive primes", primer, "up to",  limit)
    i = 0
    ctr = 0
    print("{", end="")
    while i < len(sieve):
        if sieve[i] == 1:
            print(i, end=", ")
            ctr += 1
        i += 1
    print("}")
    print("Size of field:", ctr)
    if occurances:
        print(sieve)

def create_sieve(primer, limit):
    sieve = [0 for i in range(limit + 1)]
    primer = list(map(lambda x: (x, 0), primer)) + [(0,0)]
    max_prime = 0

    while max_prime < len(primer):
        value = compute(primer)
        if value <= limit:
            sieve[value] += 1
            increment(primer, 0)
        else:
            max_prime = 0
            while value > limit:
                carry(primer, max_prime)
                value = compute(primer)
                max_prime += 1
    return sieve

sieve = create_sieve(primer, limit)
display(primer, limit, sieve, True)