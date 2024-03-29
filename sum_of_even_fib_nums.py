#############################


def fib_next(prev,curr):
    return([curr,prev+curr])

def _fib_even_sum(curr,sum):
    if(curr%2 == 0):
        sum = sum + curr
    else:
        pass
    return(sum)

def sum_of_even_fib_nums(fib_init=[1,2],maximum= 4000001):
    '''
        https://projecteuler.net/problem=2
        
        Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
        By starting with 1 and 2, the first 10 terms will be:
            1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
        By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
    '''
    s = 0
    prev,curr = fib_init
    s = _fib_even_sum(curr,s)
    prev,curr = fib_next(prev,curr)
    s = _fib_even_sum(curr,s)
    while(curr<maximum):
        prev,curr = fib_next(prev,curr)
        s = _fib_even_sum(curr,s)
    return(s)


####

# def _get_fib_format(fib_init):
    # fst,snd = fib_init
    # cond = (fst%2)*10  + (snd%2)
    # if(cond == 0):
        # return("ee")
    # if(cond == 1):
        # return("eo")
    # if(cond == 10):
        # return("oe")
    # if(cond == 11):
        # return("oo")

# def _get_fib_fst_even_index(fib_init):
    # fmt = _get_fib_format(fib_init)
    # if(fmt == "ee"):
        # return(0)
    # if(fmt == "eo"):
        # return(0)
    # if(fmt == "oe"):
        # return(1)
    # if(fmt == "oo"):
        # return(2)

# def get_fib_even_index(which,fst):
    # index = fst + which * 3
    # return(index)
