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


md = {
    1:31,
    2:28,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31
}

def is_leap_year(y):
    cond0 = (y%400 == 0)
    if(cond0):
        return(True)
    else:
        cond1 = not(y%100==0)
        cond2 = (y%4 == 0)
        cond = (cond1 and cond2)
        if(cond):
            return(True)
        else:
            return(False)

def get_days_of_month(m,y):
    if(m==2):
        cond = is_leap_year(y)
        ds = 29 if(cond) else md[2]
        return(ds)
    else:
        return(md[m])

def get_days_of_year(y):
    cond = is_leap_year(y)
    ds = 366 if(cond) else 365
    return(ds)

def get_whole_years_diff(y0,y1):
    diff = abs(y0 -y1)
    diff = (diff-1) if (diff>1) else 0
    years = list(range(y0+1,y0+diff+1)) 
    return(years)


def get_days_of_years(years):
    '''
        sum-of-days  of whole years
    '''
    ds = list(map(get_days_of_year,years))
    return(sum(ds))


def get_whole_months_diff(m0,m1):
    diff = abs(m0 -m1)
    diff = (diff-1) if (diff>1) else 0
    months = list(range(m0+1,m0+diff+1)) 
    return(months)


def get_days_of_whole_months(months,year):
    '''
        sum-of-days  of whole months
    '''
    ds = list(map(lambda m:get_days_of_month(m,year),months))
    return(sum(ds))

def get_days_head_of_month(d,m,y):
    middle_months = get_whole_months_diff(m,12)
    ds = get_days_of_whole_months(middle_months,y)
    # 5 月 30 日, 5 月一共31天 ,31 - 30 = 1天(不包括5月30日)
    head_days = get_days_of_month(m,y) - d
    ds = head_days + ds + 31
    return(ds)



#######################################################

def get_days_head(d,m,y):
    '''
        包括d,m,y当前这天
    '''
    middle_months = get_whole_months_diff(m,12)
    ds = get_days_of_whole_months(middle_months,y)
    # 5 月 30 日, 5 月一共31天 ,31 - 30 = 1天(不包括5月30日)
    head_days = get_days_of_month(m,y) - d
    ds = head_days + ds
    if(m==12):
        pass
    else:
        ds = ds + 31
    return(ds+1)

def get_days_tail(d,m,y):
    '''
        包括d,m,y当前这天
    '''
    middle_months = get_whole_months_diff(1,m)
    ds = get_days_of_whole_months(middle_months,y)
    tail_days = d
    ds = ds + tail_days
    if(m==1):
        pass
    else:
        ds = ds + 31
    return(ds)

def get_head_and_tail_year(y0,y1):
    if(y0<y1):
        return((y0,y1))
    elif(y0==y1):
        return((y0,y1))
    else:
        return((y1,y0))

def get_days_diff(dmy0,dmy1):
    '''
        包括头尾两天
    '''
    if(dmy0[2]<=dmy1[2]):
        d0,m0,y0 = dmy0
        d1,m1,y1 = dmy1
    else:
        d0,m0,y0 = dmy1
        d1,m1,y1 = dmy0
    if(y0!= y1):
        days_head = get_days_head(d0,m0,y0)
        days_tail = get_days_tail(d1,m1,y1)
        whole_years = get_whole_years_diff(y0,y1)
        days_whole = get_days_of_years(whole_years)
        ds = days_head + days_whole + days_tail
    else:
        ds = get_days_tail(d1,m1,y1) - get_days_tail(d0,m0,y0)+1
    return(ds)


def get_weekday(d,m,y):
    ds = get_days_diff((1,1,1900),(d,m,y))
    return(ds%7)
