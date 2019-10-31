import math

def is_prime(n):
    '''
        l = list(range(1,20))
        >>> list(filter(lambda ele:is_prime(ele)==True,l))
        [2, 3, 5, 7, 11, 13, 17, 19]
    '''
    if(n==1):
        return(False)
    if(n==2):
        return(True)
    uplimit = int(math.sqrt(n)) + 1
    for i in range(2,uplimit+1):
        if(n%i==0):
            return(False)
    return(True)


#########################

def find_min_prime_factor(p,n):
    uplimit = int(math.sqrt(n)) + 1
    for i in range(p,uplimit+1):
        if(is_prime(i) and (n%i == 0)):
            return((i,n//i))
    return((n,1))


def get_all_prime_factors(n):
    rslt = set({})
    p,n = find_min_prime_factor(2,n)
    rslt.add(p)
    while(n>1):
        p,n = find_min_prime_factor(p,n)
        rslt.add(p)
    return(rslt)


def largest_prime_factor(n):
    '''
        The prime factors of 13195 are 5, 7, 13 and 29.
        What is the largest prime factor of the number 600851475143 ?
    '''
    return(max(get_all_prime_factors(n)))


# 更快的算法有Pollard Rho

# def gcd(m,n):
    # r = m%n
    # if(r ==0):
        # return(n)
    # else:
        # return(gcd(n,r))
