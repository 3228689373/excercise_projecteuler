#100*(a+b) = ab +5000
# 100 可以整除ab  100 = 5*5*2*2
# 设a = 5n  n<=1  n <=200
# 1000 * 500 =(a+c)(1000-a)

def is_pythagorean(a,b,c):
    cond = a*a + b*b == c*c
    return(cond)


def get_abc():
    for a in range(1,501):
        c = 500000 // (1000-a) - a
        b = 1000-a-c
        if(b>=a  and b<=c and a*b%100==0):
            if(is_pythagorean(a,b,c)):
                print(a,b,c)
            else:
                pass
        else:
            pass
