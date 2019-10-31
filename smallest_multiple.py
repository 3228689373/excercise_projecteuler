import math
from largest_prime_factor import get_all_prime_factors


def get_diff_prime_set(si,ei):
    arr = list(range(si,ei+1))
    sts = list(map(get_all_prime_factors,arr))
    rslt = set({})
    for st in  sts:
        rslt.update(st)
    rslt = list(rslt)
    rslt.sort()
    return(rslt)


def list_mul(arr):
    rslt = 1
    for ele in arr:
        rslt = rslt * ele
    return(rslt)


def get_smallest_multiple(si,ei):
    arr = get_diff_prime_set(si,ei)
    rslt = list_mul(arr)
    return(rslt)
