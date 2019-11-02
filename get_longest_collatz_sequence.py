def kvl2d(kl,vl):
    d = {}
    for i in range(len(kl)):
        d[kl[i]]=vl[i]
    return(d)

def fmt_bignum(s):
    lns = s.split("\n")
    arr = list(map(int,lns))
    return(arr)



def collatz_next(n):
    if(n%2==0):
        n = n//2
    else:
        n = 3*n+1
    return(n)

def get_collatz_sequence(n):
    rslt = []
    while(n>1):
        n = collatz_next(n)
        rslt.append(n)
    return(rslt)

def get_collatz_step_cnt_via_refd(n):
    c = 0
    while(n>1):
        n = collatz_next(n)
        c = c + 1
    return(c)









# def reduce_2powern(kl,bl):
    # for i in range()




    # kl = list(range(1,n+1))
    # bl = list(range(1,n+1))


# def get_collatz_ref_dict(n=100):
    # kl = list(range(1,n+1))
    # vl = list(map(collatz_next,kl))
    # d = kvl2d(kl,vl)
    # return((kl,vl,d))

# kl,vl,d = get_collatz_ref_dict()
# vst = set(vl)


def get_collatz_step_cnt_via_refd(n,refd):
    c = 0
    oldn = n
    while(not(n in refd)):
        n = collatz_next(n)
        c = c + 1
    c = c + refd[n]-1
    refd[oldn] = c
    return((c,oldn))


def get_longest_collatz_sequence_le(n):
    '''
        (493, 837799)
    '''
    refd = {1:1,2:2}
    m = 2
    oldn = 2
    for i in range(1,n+1):
        c,x = get_collatz_step_cnt_via_refd(i,refd)
        if(c>m):
            m = c
            oldn=x
        else:
            pass
    return((m,oldn))
