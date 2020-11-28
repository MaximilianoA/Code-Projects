# Source:   https://www.youtube.com/watch?v=N92w4e-hrA4&ab_channel=Numberphile 
# Problem:  Find a periodic value set (Z0,c) for the function:
#           Z -> Z^2 + c
# Goal:     Ideally we want to find a set with a number of iterations s.t.
#           i > 3
#           Additionally we already know that 
#           i != 4,5

import numpy as np
from itertools import product
from math import log
from math import floor
import csv

f = lambda z,c : z**2 + c
pow_2 = lambda x : pow(2,x)
pow_4 = lambda x : pow(4,x)
log_2 = lambda x : floor(log(x, 2))
log_4 = lambda x : floor(log(x, 4)) 
MAX_RANGE = 100
ITER_MAX = 100
FILENAME = 'Facinating Fractions/output.txt'

# method to check if a value set is periodic
# if i reaches ITTER_MAX assume non-periodic
# @return: number of iterations i (-1 if non-periodic),
#          and z0 (in case of negative)
# @param: z and c MUST be of type float
def periodic(z, c):
    # TODO: instead of ITER_MAX make terminating conditions
    # TODO: instead of printing to console write to file
    z0 = z
    periodic = False
    for i in range(1, ITER_MAX):
        try:
            z = f(z, c)
            if z==z0:
                periodic = True
                break
            # z0 will always be squared in the first pass through
            # thus z0 and -z0 have the same sequence
            elif z==-z0:
                periodic = True
                z0 = -z0
                break
        except OverflowError:
            break
    if not periodic:
        i = -1
    return z0, i

# @param: accepts a float 'x'
# @return: returns that float in the most readable format
#          either as an integer or a fraction
def simplify(x):
    x_str = ''
    if float.is_integer(x):
        x_str = str(int(x))
    else:
        a,b = float.as_integer_ratio(x)
        x_str = str(a) + '/' + str(b)
    return x_str

# some simple test cases
def test():
    print('======== Periodic Examples:')
    periodic(0.0,0.0)       # eo: i=1
    periodic(1/2, 1/4)      # eo: i=1
    periodic(0.0, -1.0)     # eo: i=2
    periodic(-7/4, -29/16)  # eo: i=3
    periodic(1.0, 1.0)      # eo: non-periodic

def main():
    out_file = open(FILENAME, 'w')

    print('======== Searching')
    # From observation of previous output we see that the only
    # fractions which are successful are those where z has a 
    # denominator that is a power of two, and c has a denominator
    # with a power of 4
    # TODO: Search irrational numbers
    
    # for zd,zn in product(range(1, MAX_RANGE), range(MAX_RANGE)):
    for zd,zn in product(
        map(pow_2, range(1, log_2(MAX_RANGE)+1)),
        range(1, MAX_RANGE, 2)
        ):
        # print('z:',zn,'/',zd)

        z = zn/zd
        # check if value would have been previously examined
        _,d_min = float.as_integer_ratio(z)
        if zd!=d_min:
            continue
        
        # for cd,cn in product(range(1, MAX_RANGE), range(MAX_RANGE)):
        for cd,cn in product(
            map(pow_4, range(1, log_4(MAX_RANGE)+1)),
            range(1, MAX_RANGE, 2)
            ):
            # print('c:',cn,'/',cd)

            c = cn/cd
            # check if value would have been previously examined
            _,d_min = float.as_integer_ratio(c)
            if cd!=d_min:
                continue
            
            # Positive values
            # obviously Z^2 >= 0 t.f.
            # if c > 0 then Z^2 + c > 0 t.f.
            #   Z^2 + c <= Z (or f(x) will grow exponentially)
            #   c <= Z - Z^2
            #       if we plot y = x - x^2 we see that
            #       c <= 1/4 (see test 2)
            if c>0 and c<=1/4:
                z0, i = periodic(z,c)
                if i>0:
                    out_file.write('Z = ' + simplify(z0))
                    out_file.write('\nc = ' + simplify(c))
                    out_file.write('\ni = ' + str(i) + '\n\n')
            
            # Negative values
            c = -c
            z0, i = periodic(z,c)
            if i>0:
                out_file.write('Z = ' + simplify(z0))
                out_file.write('\nc = ' + simplify(c))
                out_file.write('\ni = ' + str(i) + '\n\n')
    out_file.close()

if __name__ == '__main__':
    main()