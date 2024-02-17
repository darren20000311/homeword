from prime_generator import PrimeGenerator


def main():
    prime_gen = PrimeGenerator()
    n = 1000000
    prime_list = prime_gen.primes_to_max(n)
    print(prime_list)


if __name__ == "__main__":
    main()
