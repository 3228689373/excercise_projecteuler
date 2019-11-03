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
from reciprocal_cycles import rm_factor



def rm_factor(n,p):
    r = n%p
    q = n//p
    while(r ==0):
        n = q
        r = n%p
        q = n//p
    return(n)


def _get_circle(n):
    lngth = len(str(n))
    i = lngth
    cond = not(int("9"*i) % n  == 0)  
    while(cond):
        i = i + 1
        cond = not(int("9"*i) % n  == 0)
    rslt = int("9"*i) // n
    return(rslt)

def get_circle(n):
    n = rm_factor(n,2)
    n = rm_factor(n,5)
    return(_get_circle(n))


def get_reciprocal_cycles_le(n):
    m = 142857
    num = 7
    for i in range(1,n):
        cycle = get_circle(i)
        if(len(str(cycle))>len(str(m))):
            m = cycle
            num = i
        else:
            pass
    return((m,num))
