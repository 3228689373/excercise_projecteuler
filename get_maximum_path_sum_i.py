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


s="""75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""


def get_left_child_loc(loc):
    x,y = loc
    x = x+1
    y = y -1
    return((x,y))

def get_right_child_loc(loc):
    x,y = loc
    x = x+1
    y = y +1
    return((x,y))

def get_parent_loc_via_left(loc):
    x,y = loc
    x = x-1
    y = y 
    return((x,y))

def get_parent_loc_via_right(loc):
    x,y = loc
    x = x-1
    y = y-1
    return((x,y))


def int_arr(arr):
    arr = list(map(int,arr))
    return(arr)

def s2nonrec_mat(s):
    lns = s.split("\n")
    lns = list(map(lambda ele:ele.split(" "),lns))
    lns = list(map(int_arr,lns))
    return(lns)


def get_maximum_path_sum_i(m):
    rslt = []
    depth = len(m) - 1
    for r in range(depth,0,-1):
        lyr = m[r]
        breadth = len(lyr)
        for c in range(0,breadth-1):
            left = lyr[c]
            right = lyr[c+1]
            px,py = get_parent_loc_via_left((r,c))
            m[px][py] = (m[px][py]+left) if(left>=right) else (m[px][py]+right)
        del m[r]
    return(m[0][0])
