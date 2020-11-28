# Source:   https://www.youtube.com/watch?v=N92w4e-hrA4&ab_channel=Numberphile
# Problem:  Find a periodic value set (Z0,c) for the function:
#           Z -> Z^2 + c
# Goal:     Ideally we want to find a set with a number of iterations s.t.
#           i > 3
#           Additionally we already know that 
#           i != 4,5

import numpy as np

f = lambda z,c: z**2 + c