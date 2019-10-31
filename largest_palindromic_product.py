import math


def is_palindromic(n):
    arr = list(str(n))
    rarr = arr[0:]
    rarr.reverse()
    cond = (arr == rarr)
    return(cond)

def get_max_bitsnum_of_product_of_nbit(nbit):
    n = int("9"*nbit)
    return(str(n*n).__len__())

def get_min_bitsnum_of_product_of_nbit(nbit):
    n = int("1" + "0"*(nbit-1))
    return(str(n*n).__len__())


def get_maxn(nbit):
    n = int("9"*nbit)
    return(n*n)

def get_minn(nbit):
    n = int("1" + "0"*(nbit-1))
    return(n*n)

def find_fst_product_of_nbit(n,nbit):
    minimum = int("1" + "0"*(nbit-1))
    maximum = int("9"*nbit)
    for i in range(minimum,maximum+1):
        if(n%i ==0):
            q = n//i
            if(q in range(minimum,maximum+1)):
                return((i,q))
            else:
                pass
        else:
            pass
    return(None)

def get_largest_palindromic(nbit):
    '''
        A palindromic number reads the same both ways. 
        The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
        Find the largest palindrome made from the product of two 3-digit numbers.
    '''
    si = get_minn(nbit)
    ei = get_maxn(nbit)
    for i in range(ei,si-1,-1):
        cond = is_palindromic(i)
        if(cond):
            r0 = find_fst_product_of_nbit(i,nbit)
            if(r0!= None):
                return(r0)
            else:
                pass
        else:
            pass
    return(None)
