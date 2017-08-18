from collections import namedtuple
from math import sqrt

Point = namedtuple('Point', 'x y')
CartesianPoint = namedtuple('CartesianPoint', ['x', 'y'])
PolarPoint = namedtuple('PolarPoint', ['r', 'theta'])


def distance(p):
    if isinstance(p, CartesianPoint):
        return sqrt(p.x**2 + p.y**2)
    elif isinstance(p, PolarPoint):
        return p.r
    else:
        raise TypeError

my_p = CartesianPoint(9, 9)
d = distance(my_p)
print 'The distance is {}'.format(d)
