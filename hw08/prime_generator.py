class PrimeGenerator:
    def primes_to_max(self, n):
        # Create  an empty list to store the prime numbers
        PRIME_NUMBERS = []
        # I initialize the all numbers to be prime numbers at first.
        is_prime = [True] * (n + 1)
        # Because 1 is not a prime number, so in for loop
        # it should begins with 2.
        # n + 1 is because we need to contain the last number in the loop.
        for num in range(2, n+1):
            if is_prime[num]:
                for multiplys in range(num * num, n+1, num):
                    is_prime[multiplys] = False
                PRIME_NUMBERS.append(num)
                # We start from num * num is because any smaller multiple
                # of num has already mark as non-prime numbers.
                # And then, num is step size,
                # and then the multiply of num is all non-prime numbers.
                # for multiplys in range(num * num, n+1, num):
                #     is_prime[multiplys] = False
        return PRIME_NUMBERS
