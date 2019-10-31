def sum_of_mul_of_3or5(n=1000):
    '''
        https://projecteuler.net/problem=1
        If we list all the natural numbers below 10 that are multiples of 3 or 5, 
        we get 3, 5, 6 and 9. The sum of these multiples is 23.
        Find the sum of all the multiples of 3 or 5 below 1000.
    '''
    arr = list(range(1,n+1))
    arr3 = list(filter(lambda ele:ele%3==0,arr))
    arr5 = list(filter(lambda ele:ele%3==0,arr))
    arr = arr3 + arr5
    rslt = sum(arr)
    return(sum)
