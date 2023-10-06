# Program Spec: Given an array A[] of integers, write a program to find the
# Maximum difference between any two elements such that the larger element
# Appears after the smaller element. In other words, it needs to find
# max(A[j] - A[i]) where A[j] > A[i] and j > i
# Input: A[] = [1,4,9,5,3,7] -> Output: 8
# (Because maximum difference is between 9 and 1)
# Input: A[] = [9,8,1,6,3,2] -> Output: 5
# (Because maximum difference is between 6 and 1)
# Input: A[] = [9,8,6,3,2] -> Output: -1
# (Because A[j] is never > A[i])

# # Time Complexity is O(n^2)
# def max_difference(list):
#     num = len(list)
#     min_value = list[0]
#     for i in range(num - 1):
#         for j in range(i + 1, num):
#             if list[j] > list[i]:
#                 max_diff = max(max_diff, list[j] - list[i])
#     return max_diff


# Time Complexity is O(n)
def max_difference(list):
    num = len(list)
    min_value = list[0]
    max_diff = -1
    for i in range(1, num):
        if (list[i] - min_value) > max_diff:
            max_diff = list[i] - min_value
        if list[i] < min_value:
            min_value = list[i]
    return max_diff

def main():

    list = [9,8,1,6,3,2]
    ans = max_difference(list)
    print(ans)

main()