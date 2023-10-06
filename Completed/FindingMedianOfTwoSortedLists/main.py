from typing import List

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    a, b = (nums1, nums2) if len(nums1) <= len(nums2) else (nums2, nums1)
    N, M = len(a), len(b)  # M >= 1

    total_len = N + M

    # number of elements below and including the smallest median element
    num_to_take = (total_len + 1) // 2

    # n is how many taken from a, m is how many taken from b

    lo = 0
    hi = min(N, num_to_take)
    # compute partition_point(a, lo, hi, need_more_from_a)
    while lo < hi:
        n = (lo + hi) // 2
        m = num_to_take - n
        if m > 0 and b[m - 1] > a[n]:
            lo = n + 1
        else:
            hi = n

    n = lo
    m = num_to_take - n

    # max(a[:n] + b[:m])
    curr = a[n - 1] if m == 0 or n > 0 and a[n - 1] >= b[m - 1] else b[m - 1]

    if total_len % 2:
        return curr # * 1.0 if you _really_ want to return a float

    # min(a[n:] + b[m:])
    nxt = a[n] if m == M or n < N and a[n] <= b[m] else b[m]

    return (curr + nxt) / 2

if __name__ == '__main__':
    list1 = [1, 3, 5, 7, 9, 62, 51]
    list2 = [2, 6, 22, 34, 45, 55]

    print(findMedianSortedArrays(list1, list2))
    # Ex:  [1, 2, 3, 5, 6, 7, 9, 22, 34, 45, 55] = 7