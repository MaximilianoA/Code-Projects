# Source:   https://www.youtube.com/watch?v=N92w4e-hrA4&ab_channel=Numberphile
# Problem:  Find a periodic value set (Z0,c) for the function:
#           Z -> Z^2 + c
# Goal:     Ideally we want to find a set with a number of iterations s.t.
#           i > 3
#           Additionally we already know that 
#           i != 4,5

import numpy as np
from itertools import product

f = lambda z,c: z**2 + c
ITER_MAX = 30

# method to find number of iterations i
# if i reaches ITTER_MAX assume non-periodic
# @return: weather or not these values are periodic
# @param: z and c MUST be of type float
# TODO: instead of ITER_MAX make terminating conditions
# TODO: instead of printing to console write to file
def check_if_periodic(z, c, view=False):
    z0 = z
    periodic = False
    for i in range(1, ITER_MAX):
        try:
            z = f(z, c)
            if view:
                print(simplify(z))
            if z==z0:
                periodic = True
                break
            # z0 will always be squared in the first pass through
            # thus z0 and -z0 have the same sequence
            elif -z==z0:
                periodic = True
                z0 = -z
                break
        except OverflowError:
            break
    if periodic:
        print('Z =', simplify(z0))
        print('c =', simplify(c))
        print('i =', i, '\n')
    elif view:
        print('non-periodic\n')
    return periodic

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
    check_if_periodic(0.0,0.0)       # eo: i=1
    check_if_periodic(1/2, 1/4)      # eo: i=1
    check_if_periodic(0.0, -1.0)     # eo: i=2
    check_if_periodic(-7/4, -29/16)  # eo: i=3
    check_if_periodic(1.0, 1.0)      # eo: non-periodic

def main():
    print('======== Searching')
    # Theory: in order for the function to be periodic it
    #         must either converge or oscilate

    # for each possible z
    for zn,zd in product(range(30), range(1, 30)):
        z = zn/zd

        # check if value would have been previously examined
        _,d_min = float.as_integer_ratio(z)
        if zd!=d_min:
            continue
        
        # for each possible c
        for cn,cd in product(range(30), range(1,30)):
            c = cn/cd

            # check if value would have been previously examined
            _,d_min = float.as_integer_ratio(c)
            if cd!=d_min:
                continue

            # obviously Z^2 >= 0 t.f.
            # if c > 0 then Z^2 + c > 0 t.f.
            #   Z^2 + c <= Z (or f(x) will grow exponentially)
            #   c <= Z - Z^2
            #       if we plot y = x - x^2 we see that
            #       c <= 1/4 (see test 2)
            if c < 1/4:
                check_if_periodic(z,c)
            


if __name__ == '__main__':
    main()