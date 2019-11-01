import math
from largest_prime_factor import get_all_prime_factors
from operator import itemgetter

def select_seqs(ol,seqs):
    '''
        from elist.elist import *
        ol = ['a','b','c','d']
        select_seqs(ol,[1,2])
    '''
    rslt = itemgetter(*seqs)(ol)
    if(seqs.__len__()==0):
        rslt = []
    elif(seqs.__len__()==1):
        rslt = [rslt]
    else:
        rslt = list(rslt)
    return(rslt)


def get_sum_of_combination_product(arr):
    iters = itertools.combinations(arr,2)
    s = 0
    for it in iters:
        s = it[0]*it[1] + s
    return(s)

def sum_square_difference(n):
    arr = list(range(1,n+1))
    s = get_sum_of_combination_product(arr)
    return(2*s)
