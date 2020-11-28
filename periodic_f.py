# Source:   https://www.youtube.com/watch?v=N92w4e-hrA4&ab_channel=Numberphile
# Problem:  Find a periodic value set (Z0,c) for the function:
#           Z -> Z^2 + c
# Goal:     Ideally we want to find a set with a number of iterations s.t.
#           i > 3
#           Additionally we already know that 
#           i != 4,5

import numpy as np

f = lambda z,c: z**2 + c
ITER_MAX = 30

# method to find number of iterations i
# if i reaches ITTER_MAX assume non-periodic
# @return: weather or not these values are periodic
# @param: z and c MUST be of type float
def test_if_periodic(z, c, view=False):
    z0 = z
    periodic = False
    for i in range(1, ITER_MAX):
        z = f(z, c)
        if view:
            print(z)
        if z==z0:
            periodic = True
            break
    if periodic:
        print(
            'Z =', z0,
            '\tc =', c,
            '\ti =', i, 
            )
    else:
        print('non-periodic')
    return periodic

# TEST
test_if_periodic(0.0,0.0)       # eo: i=1
test_if_periodic(1/2, 1/4)      # eo: i=1
test_if_periodic(0.0, -1.0)     # eo: i=2
test_if_periodic(-7/4, -29/16)  # eo: i=3
# test_if_periodic(1.0, 1.0)      # eo: non-periodic