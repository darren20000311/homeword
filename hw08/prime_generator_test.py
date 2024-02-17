from prime_generator import PrimeGenerator


def test_primes_to_max():
    prime_gen = PrimeGenerator()

    assert prime_gen.primes_to_max(10) == [2, 3, 5, 7]
    assert prime_gen.primes_to_max(20) == [2, 3, 5, 7, 11, 13, 17, 19]


test_primes_to_max()
