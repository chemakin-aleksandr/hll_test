test_data = [
    ([1, 2, 3, 4], 0),
    ([4, 3, 2, 1], 0),
    ([2, 1, 3, 4], 0),
    ([4, 3, 1, 2], 0),
    ([1, 6, 3, 4, 5], 1),
    ([1, 3, 6, 4, 5], 2),
    ([1, 3, 4, 7, 6, 5], 3),
    ([3, 1, 4, 7, 6, 5], 3),
    ([-1, -2, -3, -4], 0),
    ([-4, -3, -2, -1], 0),
    ([-4, -3, 2, 1], 1),
    ([1, -2, 3, -4], 1),
    ([5, 2, 7, 0], 1),
    ([1, 2, 7, 0], 2),
    ([3, 2, 4, 8, 7, 6, 5, 1], 10),
]

"""
[3, 2, 4, 8, 7, 6, 5, 1]
1. [3, 2, 8, 4, 7, 6, 5, 1]
2. [3, 8, 2, 4, 7, 6, 5, 1]
3. [8, 3, 2, 4, 7, 6, 5, 1]
4. [8, 3, 2, 4, 6, 7, 5, 1]   4. [8, 3, 2, 7, 4, 6, 5, 1]
5. [8, 3, 2, 4, 6, 5, 7, 1]   5. [8, 3, 7, 2, 4, 6, 5, 1]     
6. [8, 3, 2, 4, 6, 5, 1, 7]   6. [8, 7, 3, 2, 4, 6, 5, 1]
7. [8, 3, 2, 4, 5, 6, 1, 7]   7. [8, 7, 3, 2, 4, 5, 6, 1]
8. [8, 3, 2, 4, 5, 1, 6, 7]   8. [8, 7, 3, 2, 4, 5, 1, 6]
9. [8, 3, 2, 4, 1, 5, 6, 7]   9. [8, 7, 3, 2, 4, 1, 5, 6]
10. [8, 3, 2, 1, 4, 5, 6, 7] 10. [8, 7, 3, 2, 1, 4, 5, 6]
"""


def shift_el(a, f, t):
    # [3, 2, 8] 2 -> 0
    i = 1
    if f > t:
        i = -1
    while f != t:
        a[f], a[f + i] = a[f + i], a[f]
        f += i


def find_max_i(a, lo, hi):
    m = a[lo]
    mi = -1
    for i in range(lo, hi):
        if a[i] > m:
            m = a[i]
            mi = i

    return mi


def check(a):
    pass


def n_swaps(a):
    lo = 0
    hi = len(a) - 1
    min_swaps = 0
    while hi - lo > 0:
        max_i = find_max_i(a, lo, hi + 1)
        if max_i == -1:
            break
        if abs(max_i - lo) > abs(max_i - hi):
            min_swaps += abs(max_i - hi)
            shift_el(a, max_i, hi)
            hi -= 1
        else:
            min_swaps += abs(max_i - lo)
            shift_el(a, max_i, lo)
            lo += 1

    return min_swaps


if __name__ == '__main__':
    for t in test_data:
        test_array, test_value = t
        print(f'Testing {test_array} -> {test_value}: ', end='')
        try:
            calc_value = n_swaps(test_array)
            assert calc_value == test_value
        except AssertionError:
            print(f'FAIL: expected {test_value} but calc {calc_value}')
            continue
        print('OK')
