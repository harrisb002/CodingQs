# Program Spec: Given an array of integers and a value targetSum
# Write a program to determine whether there is a pair of elements
# In the array that sum exactly to targetSum. In other words,
# Need to determine whether two elements exist in the array
# Whose sum is equal to targetSum.
# All elements are distinct and can be pos. or neg.
# Input: X[] = [-5,1,-40,20,6,8,7]  TargetSum = 15  -> Output: True

# Time Complextiy = O(n^2)
# def findPairSum(list, targetSum):
#     num = len(list)
#     for i in range(num):
#         for j in range(i+1, num):
#             sum = list[i] + list[j]
#             if (targetSum == sum):
#                 return True
#
#     return False

# # Time Complextiy = O(nlogn) + O(nlogn) = O(nlogn)
# def findPairSum(list, targetSum):
#     list = insertionSort(list)
#     start = 0
#     end = len(list) - 1
#     while start <= end:
#         if list[start] + list[end] == targetSum:
#             return True
#         elif list[start] + list[end] < targetSum:
#             start+=1
#         else:
#             end -=1
#     return False
#
# def insertionSort(list):
#     num = len(list)
#     for i in range(1, num):
#         curr_value = list[i]
#         j = i - 1
#         while(j >= 0 and list[j] > curr_value):
#             list[j+1] = list[j]
#             j-=1
#         list[j+1] = curr_value
#     return list

# Using Hash table is O(n) time complexity
def findPairSum(list, targetSum):
    num = len(list)
    H = {}
    for i in range(num):
        k = targetSum - list[i]
        if k in H:
            return True
        H[list[i]] = True
    return False

def main():
    list = [-5, 1, -40, 20, 6, 8, 8]
    targetSum = 15
    ans = findPairSum(list, targetSum)
    print(ans)

main()














