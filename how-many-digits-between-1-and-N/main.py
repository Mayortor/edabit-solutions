import Test

def digits(n):
    c = 0
    i = 0
    n = n - 1
    a = 9 * (10 ** i)
    while (n > 9 * (10 ** i)):
        n -= 9 * (10 ** i)
        c += 9 * (10 ** i) * (i + 1)
        i += 1
    c += n * (i + 1)
    return c

Test.assert_equals(digits(1), 0)
Test.assert_equals(digits(10), 9)
Test.assert_equals(digits(100), 189)
Test.assert_equals(digits(2020), 6969)
Test.assert_equals(digits(103496754), 820359675)
Test.assert_equals(digits(3248979384), 31378682729)
Test.assert_equals(digits(122398758003456), 1724870258940729)
Test.assert_equals(digits(58473029386609125789), 1158349476621071404669)
