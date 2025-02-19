import sys
import math

# check if is prime
def is_prime(num):
    # search for primes
    i = num - 1
    while (i > 1):
        # if it divides evenly with any factor then its not prime
        if ((num % i) == 0):
            return False
        i=i-1
    return True

# iterate through each number checking for primes
def n_primes(n):
    count = 0
    num = 2

    while (count < n):
        if is_prime(num):
            print(num)
            count= count + 1
        num = num + 1


# driver function
def main():
    n = int(sys.argv[1])
    n_primes(n)

if __name__ == "__main__":
    main()