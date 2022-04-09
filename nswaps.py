"""
Дан массив различных целых чисел.
Мы хотим отсортировать его следующим образом:
a0 > a1 > a2 > … > a_{k-1} > a_k < a_{k+1} < a_{k+2} < … a_N, 0 <= k <= N.

При этом единственная допустимая операция:
    поменять местами два соседних элемента.

Необходимо написать функцию вида def n_swaps(l),
    возвращающую минимально необходимое количество операций,
    которые приводят массив к данному виду.

Обращаю внимание, что индекс k может быть с краю
    (то есть, отсортированный список уже обладает нужным порядком элементов),
    а также что k не является параметром функции,
    а должен получаться в результате работы алгоритма.

Пользовался следующими ресурсами:

https://stackoverflow.com/questions/20990127/sorting-a-sequence-by-swapping-adjacent-elements-using-minimum-swaps
https://www.geeksforgeeks.org/counting-inversions/
https://stackoverflow.com/questions/337664/counting-inversions-in-an-array/6424847#6424847


"""
import math
from heapq import heappush, heappop
from bisect import bisect, insort

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
]


def _calc_swaps(heap_list, top_down=False):
    x = []
    m = 0
    b = 0
    while heap_list:  
        _, i = heappop(heap_list) 
        y = bisect(x, i) 
        m += y
        b += i - y
        insort(x, i) 

    result = b
    if top_down:
        result = m

    return result


def count_inversions(a, k, limit):
    left_side_sorted = []
    for i in range(k + 1):
        heappush(left_side_sorted, (a[i], i))

    min_el = a[left_side_sorted[0][1]]

    left_side_swaps = _calc_swaps(left_side_sorted, True)
    right_side_swaps = math.inf
    right_side_sorted = []
    if left_side_swaps < limit:
        heappush(right_side_sorted, (min_el, 0))
        for i in range(k + 1, len(a)):
            heappush(right_side_sorted, (a[i], i - k))

        right_side_swaps = _calc_swaps(right_side_sorted)

    left_to_right_swaps = left_side_swaps + right_side_swaps

    # cals swaps from right to left
    for i in range(k, len(a)):
        heappush(right_side_sorted, (a[i], i - k))

    min_el = right_side_sorted[0][0]
    right_side_swaps = _calc_swaps(right_side_sorted)
    left_side_swaps = math.inf
    if right_side_swaps < limit:
        for i in range(k):
            heappush(left_side_sorted, (a[i], i))

        heappush(left_side_sorted, (min_el, k))

        left_side_swaps = _calc_swaps(left_side_sorted, True)

    right_to_left_swaps = left_side_swaps + right_side_swaps

    return min(left_to_right_swaps, right_to_left_swaps)


def n_swaps(a):
    min_swaps = math.inf

    for k in range(len(a)):
        swaps = count_inversions(a, k, min_swaps)
        if min_swaps > swaps:
            min_swaps = swaps

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
