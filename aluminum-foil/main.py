import Test
import math

def myround(x, prec=8, base=.0001):
  return round(base * round(float(x)/base),prec)

ALUM_THINKNESS = myround(0.0025)

def foil(l):
    PI = math.pi
    d = 4.0

    while (l > 0):
        next = (d / 2) * 2 * PI
        l -= next
        d += ALUM_THINKNESS * 2

    return myround(d)

#Tests
Test.assert_equals(foil(0), 4.0)
Test.assert_equals(foil(6), 4.0025)
Test.assert_equals(foil(7), 4.005)
Test.assert_equals(foil(12), 4.005)
Test.assert_equals(foil(13), 4.0075)
Test.assert_equals(foil(1000), 4.3825)
Test.assert_equals(foil(7777), 6.385)
Test.assert_equals(foil(123456), 20.2275)
