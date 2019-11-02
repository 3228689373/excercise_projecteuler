import math
import copy
import itertools
from largest_prime_factor import get_all_prime_factors,is_prime
from sum_square_difference import select_seqs
from the_10001st_prime import is_prime_via_prev_prime_set,get_prime_list,get_primes_list3
from largest_product_in_a_series import get_largest_product_in_a_series,get_win_arr,mul_arr
from largest_product_in_a_grid import transpose,fmt2mat
from longest_collatz_sequence import kvl2d
from lattice_paths import init_mat
from maximum_path_sum import int_arr
from amicable_numbers import get_sum_of_factors
from non_abundant_sums import get_sum_of_factors


def bitsnum(n):
    return(len(str(n)))

def fib_next(prev,curr):
    return([curr,prev+curr])

def find_fst_ge_nbits(n):
    prev = 1
    curr = 1
    nbits = bitsnum(curr)
    while(nbits<n):
        prev,curr=fib_next(prev,curr)
        nbits = bitsnum(curr)
    return((prev,curr))
