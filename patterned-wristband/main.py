import Test

def is_horizontal(lst):
	for y in lst:
		for x in y:
			if (x != y[0]):
				return False
	return True

def is_vertical(lst):
	for y in range(len(lst)):
		for x in range(len(lst[y])):
			if (lst[y][x] != lst[0][x]):
				return False
	return True

def is_diagonal_left(lst):
	for y in range(1, len(lst)):
		for x in range(1, len(lst[y])):
			if (lst[y][x] != lst[y - 1][x - 1]):
				return False
	return True

def is_diagonal_right(lst):
	for y in range(1, len(lst)):
		for x in range(len(lst[y]) - 1):
			if (lst[y][x] != lst[y - 1][x + 1]):
				return False
	return True

def is_wristband(lst):
	return (is_horizontal(lst) or is_vertical(lst) or is_diagonal_left(lst) or is_diagonal_right(lst))

Test.assert_equals(is_wristband(
[['A', 'A'],
['B', 'B'],
['C', 'C']]), True)

Test.assert_equals(is_wristband(
[['A', 'B'],
['A', 'B'],
['A', 'B']]), True)

Test.assert_equals(is_wristband(
[['A', 'B', 'C'],
['C', 'A', 'B'],
['B', 'C', 'A'],
['A', 'B', 'C']]), True)

Test.assert_equals(is_wristband(
[['A', 'B', 'C'],
['C', 'A', 'B'],
['D', 'C', 'A'],
['E', 'D', 'C']]), True)

Test.assert_equals(is_wristband(
[['A', 'B', 'C'],
['B', 'A', 'B'],
['D', 'C', 'A'],
['E', 'D', 'C']]), False)

Test.assert_equals(is_wristband(
[['A', 'B', 'C'],
['B', 'C', 'A'],
['C', 'A', 'B'],
['A', 'B', 'A']]), True)

Test.assert_equals(is_wristband(
[['A', 'B', 'C'],
['B', 'C', 'D'],
['C', 'D', 'E'],
['D', 'E', 'F']]), True)

Test.assert_equals(is_wristband(
[['A', 'B', 'C'],
['B', 'C', 'D'],
['C', 'D', 'E'],
['D', 'E', 'E']]), True)

Test.assert_equals(is_wristband(
[['A', 'B', 'C'],
['B', 'C', 'D'],
['C', 'D', 'E'],
['D', 'F', 'E']]), False)

Test.assert_equals(is_wristband(
[['A', 'B', 'C'],
['B', 'D', 'A'],
['C', 'A', 'B'],
['A', 'B', 'A']]), False)

Test.assert_equals(is_wristband(
[['A', 'B'],
['A', 'B'],
['A', 'C'],
['A', 'B']]), False)

Test.assert_equals(is_wristband(
[['A', 'A'],
['B', 'B'],
['C', 'C'],
['D', 'B']]), False)

Test.assert_equals(is_wristband(
[['A', 'A'],
['B', 'B'],
['C', 'C'],
['C', 'C']]), True)
