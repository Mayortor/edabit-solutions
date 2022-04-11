import Test

def lcm(arr):
    arr.sort()
    max = arr[-1]
    multi = 1
    for i in arr:
        multi *= i
    c = 2
    while (found == False):
        found = True
        n += max
        for i in arr:
            if not (n % i == 0):
                found = False

    return n


#Tests
Test.assert_equals(lcm([1]), 1)
Test.assert_equals(lcm([5, 5, 5]), 5)
Test.assert_equals(lcm([67, 34, 12, 3, 2]), 13668)
Test.assert_equals(lcm([79, 18, 7, 3, 1]), 9954)
Test.assert_equals(lcm([10, 20, 30, 40, 50]), 600)
Test.assert_equals(lcm([2, 3, 5, 7, 11, 13, 17]), 510510)
Test.assert_equals(lcm([91, 92, 93, 94, 95]), 3476431140)
