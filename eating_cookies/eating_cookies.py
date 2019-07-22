#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution
new_cache = {
    1: 1,
    2: 2,
    3: 4,
    4: 7
}


def eating_cookies(n, cache=None):
    if n < 1:
        return 1
    if n in new_cache:
        return new_cache[n]
    else:
        new_cache[n] = eating_cookies(
            n-1, new_cache) + eating_cookies(n-2, new_cache) + eating_cookies(n-3, new_cache)
    return new_cache[n]


# print(eating_cookies(45))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
