import math
import copy
from largest_prime_factor import get_all_prime_factors,is_prime
from sum_square_difference import select_seqs
from the_10001st_prime import is_prime_via_prev_prime_set,get_prime_list,get_primes_list3
from largest_product_in_a_series import get_largest_product_in_a_series,get_win_arr,mul_arr
from largest_product_in_a_grid import transpose,fmt2mat
from longest_collatz_sequence import kvl2d
from lattice_paths import init_mat



# sum(list(map(int,list(str(2 ** 1000)))))

d0 = {
   1:"one",
   2:"two",
   3:"three",
   4:"four",
   5:"five",
   6:"six",
   7:"seven",
   8:"eight",
   9:"nine"
}

d1 = {
   10:"ten",
   11:"eleven",
   12:"twelve",
   13:"thirteen",
   14:"fourteen",
   15:"fifteen",
   16:"sixteen",
   17:"seventeen",
   18:"eighteen",
   19:"nineteen"
}


d2 = {
   2:"twenty",
   3:"thirty",
   4:"fourty",
   5:"fifty",
   6:"sixty",
   7:"seventy",
   8:"eighty",
   9:"ninty"
}


def _twobitsnum2str(kl):
    print(kl)
    if(kl[0] == 0 and kl[1] == 0):
        return("")
    elif(kl[0] == 0 and kl[1] != 0):
        return(d0[kl[1]])
    else:
        if(kl[0]==1):
            return(d1[10*kl[0]+kl[1]])
        else:
            s = d2[kl[0]]+d0[kl[1]]  if(kl[1]>0) else d2[kl[0]]
            return(s)



def num2str(n):
    kl = list(map(int,list(str(n))))
    lngth = len(kl)
    if(lngth == 3):
        s = d0[kl[0]] + "hundred" 
        s1 = _twobitsnum2str(kl[1:])
        s = s + s1 if(s1=="") else (s+"and"+s1)
        return(s)
    elif(lngth == 2):
        if(kl[0]==1):
            return(d1[10*kl[0]+kl[1]])
        else:
            s = d2[kl[0]]+d0[kl[1]]  if(kl[1]>0) else d2[kl[0]]
            return(s)
    else:
        return(d0[kl[0]])



def get_number_letter_counts(n):
    if(n==1000):
        return(len("one thousand"))
    else:
        s = num2str(n)
        return(len(s))
