# Sieve of Eratosthenes
# Given a range of 2 numbers (i.e) L and R count the number of prime numbers in the range (inclusive of L and R ).

# A prime number is a number greater than 1 that has only two divisors: 1 and itself.
# Instead of checking if each number in n is prime, we eliminate numbers in n that are NOT prime, by first verifying what sqrt(n) is
# and then start sieving(dropping multiples) for the range(sqrt(n)). Once completed for that range, the remaining the numbers in that
# range are the prime numbers.
import math
L, R = map(int, input().split())

def sieve_of_eratosthenes(R):
    is_prime = [True] * (R + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(math.sqrt(R)) + 1):
        if is_prime[i]:
            for j in range(i * i, R + 1, i): # i * i as smaller multiples were already marked by smaller primes.
                is_prime[j] = False

    return is_prime

is_prime = sieve_of_eratosthenes(R)

result = [i for i in range(max(L, 2), R + 1) if is_prime[i]]
print(len(result))