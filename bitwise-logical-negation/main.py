import Test

def compress(arr):
    result = ''
    counter = 0
    i = 0
    while (i < (len(arr) - 1)):
        if (arr[i] == arr[i + 1]):
            counter += 1
        else:
            if (counter == 0):
                result += arr[i]
            else:
                result += arr[i] + str(counter + 1)
            counter = 0
        i += 1
    if (counter == 0):
        result += arr[i]
    else:
        result += arr[i] + str(counter + 1)
    return result

from time import perf_counter
from random import randint
tic = perf_counter()

Test.assert_equals(compress(["a", "a", "b", "b", "c", "c", "c"]), "a2b2c3")
Test.assert_equals(compress(["a"]), "a")
Test.assert_equals(compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]), "ab12")
Test.assert_equals(compress(["a", "a", "a", "b", "b", "a", "a"]), "a3b2a2")

t_fun = 0
for _ in range(20):
    arr = []
    expected = []
    for idx in range(randint(1, 200)):
        c = chr(97 + idx % 26)
        len_c = randint(1, 200)
        arr += [c] * len_c
        expected.append(c)
        if len_c > 1:
            expected.append(str(len_c))

    tic_fun = perf_counter()
    """function call"""
    Test.assert_equals(compress(arr), "".join(expected))
    t_fun += perf_counter() - tic_fun

print('t_fun = {:.6f}'.format(t_fun))
print('Total = {:.6f}'.format(perf_counter() - tic))
