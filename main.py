def f(t):
    return 2 * math.exp(-8*abs(t))

from draw_function import *
draw_function(f, -10, 10)
