import math
import copy
from largest_prime_factor import get_all_prime_factors,is_prime
from sum_square_difference import select_seqs
from the_10001st_prime import is_prime_via_prev_prime_set,get_prime_list,get_primes_list3
from largest_product_in_a_series import get_largest_product_in_a_series,get_win_arr,mul_arr
from largest_product_in_a_grid import transpose,fmt2mat
from longest_collatz_sequence import kvl2d
from lattice_paths import init_mat


def init_mat(r,c):
    m = [[]] * (r)
    m = list(map(lambda r:[None]*(c),m))
    return(m)

def get_lattice_paths(n):
    m = init_mat(n+1,n+1)
    m[0] = list(map(lambda ele:1,m[0]))
    for r in m:
        r[0] = 1
    for r in range(1,n+1):
        for c in range(1,n+1):
            m[r][c] = m[r-1][c] + m[r][c-1]
    return(m)
