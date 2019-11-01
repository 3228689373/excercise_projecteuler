import math
import copy
from largest_prime_factor import get_all_prime_factors,is_prime
from sum_square_difference import select_seqs
from the_10001st_prime import is_prime_via_prev_prime_set,get_prime_list,get_primes_list3
from largest_product_in_a_series import get_largest_product_in_a_series,get_win_arr,mul_arr
from largest_product_in_a_grid import transpose,fmt2mat


def get_triangle_number(which):
    if(which==0):
        return(1)
    else:
        return(which*(which+1)//2)


def get_divisors_num(n):
    '''
        因为三角数 = n*(n+1)/2 ,n为偶数(m)*(2m+1)     n为奇数(m+1)*(2m+1)
        n * (n+1) 的 因数 f 一定是 n*(n+1) /2 的因数
        n 的因数如果为 1=<f0,f1.....fm <=n, 则n*(n+1)的因数 必然为 x*y ,如果其中有一个 >=n+1
        那么只能是fi * (n+1) 的形式，假如有一个数不是这种形式,只可能为:
            1 . (n+1)(n+1)>n*(n+1)
            2 .  fi * (n+a)   a>=2 and a <=n,那么n=fi*k  k(n+1)==n+a   n(k-1) == a-1 <= n-1  所以k==1 ,a==1矛盾
        所以n*(n+1) 因数个数 =
           n 的因数个数 * 2
    '''
    if(n==1):
        return(1)
    sq = int(math.sqrt(n))
    c = 0
    for i in range(1,sq+1):
        if(n%i==0):
            c = c +1
        else:
            pass
    return(c*2)


def highly_divisible_triangular_number(divisors_num=500):
    c = 0
    which = 1
    while(c<divisors_num+1):
        n = get_triangle_number(which)
        c = get_divisors_num(n)
        which = which + 1
        print(n,c)
    return(n)

#https://blog.csdn.net/u010565244/article/details/20070625

# def highly_divisible_triangular_number2(divisors_num=500):
    # which = 2000
    # n = get_triangle_number(which)
    # c = get_divisors_num(n)
    # while(c<divisors_num+1):
        # which = which +2000 
        # n = get_triangle_number(which)
        # c = get_divisors_num(n)
        # print(c)
    # return(n)


# def get_prime_divisors(n):
    # p_factors = get_all_prime_factors(n)
    # d = {}
    # while(n>1):
        # np_factors = copy.deepcopy(p_factors)
        # for p in p_factors:
            # if(n%p==0):
                # if(p in d):
                    # d[p] = d[p] + 1
                # else:
                    # d[p] = 1
                # n = n//p
            # else:
                # np_factors.remove(p)
        # p_factors = np_factors
    # return(d)

# def get_divisors_num(n):
    # d = get_prime_divisors(n)
    # rslt = 1
    # for k in d:
        # v =d[k]
        # rslt = rslt*(v+1)
    # return(rslt)
