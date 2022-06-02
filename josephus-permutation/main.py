import Test

def who_goes_free(n, k):
	circle = list(range(n))
	i = 0
	while (len(circle) != 1):
		i += (k - 1)
		while (i >= len(circle)):
			i -= len(circle)
		circle.pop(i)
	return int(circle[0])

Test.assert_equals(who_goes_free(9, 2), 2)
Test.assert_equals(who_goes_free(9, 3), 0)
Test.assert_equals(who_goes_free(7, 2), 6)
Test.assert_equals(who_goes_free(7, 3), 3)
Test.assert_equals(who_goes_free(15, 4), 12)
Test.assert_equals(who_goes_free(14, 3), 1)
Test.assert_equals(who_goes_free(53, 7), 21)
Test.assert_equals(who_goes_free(543, 21), 455)
Test.assert_equals(who_goes_free(673, 13), 303)
