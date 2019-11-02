import math
import copy
from largest_prime_factor import get_all_prime_factors,is_prime
from sum_square_difference import select_seqs
from the_10001st_prime import is_prime_via_prev_prime_set,get_prime_list,get_primes_list3
from largest_product_in_a_series import get_largest_product_in_a_series,get_win_arr,mul_arr
from largest_product_in_a_grid import transpose,fmt2mat
from longest_collatz_sequence import kvl2d
from lattice_paths import init_mat
from maximum_path_sum import int_arr


#sum(int_arr(list(str(math.factorial(100)))))

def get_sum_of_factors(n):
    sm = 1
    for i in range(2,n):
        v = i if(n%i==0) else 0
        sm = sm + v
    return(sm)


def get_amicable_numbers(n):
    '''
        {1184, 6368, 5564, 5020, 2924, 284, 6232, 1210, 220, 2620}
    '''
    st = set({})
    for i in range(2,n):
        smf0 = get_sum_of_factors(i)
        smf1 = get_sum_of_factors(smf0)
        if(i ==smf1 and i!=smf0 and not(i in st)):
            # ele = [i,smf0]
            # ele.sort()
            st.add(i)
            st.add(smf0)
        else:
            pass
    return(st)
