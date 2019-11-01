import math
from largest_prime_factor import get_all_prime_factors,is_prime
from sum_square_difference import select_seqs
from the_10001st_prime import is_prime_via_prev_prime_set,get_prime_list,get_primes_list3


def summation_of_primes_le(n=2000000):
    primes = get_primes_list3(n)
    return(sum(primes))
