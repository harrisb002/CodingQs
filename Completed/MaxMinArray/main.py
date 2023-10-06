# Program Spec: Given an array X[] of size n
# Find the max and min elements in array
# Using minimum amount of comparisons as possible

# Worst-case assorted in des. order and 2*(n-1) comparisons, i:e 2n-2 will be made
# Time Complexity is O(n)
# def max_min(list):
#     num = len(list)
#     if num == 0:
#         return 0,0
#
#     max, min = list[0], list[0]
#     if num == 1:
#         return max, min
#
#     for i in range(num - 1):
#         if list[i+1] > max:
#             max = list[i+1]
#         elif list[i+1] < min:
#             min = list[i+1]
#
#     return max, min

# Total comparisons 3n/2 -2 may be made, better than above
# Time Complexity is O(n), same as above
# def max_min(list, start, end):
#     max, min = 0, list[0]
#     # Base Cases, 1 or 2 elements in array
#     if start == end:
#         return max, min
#     elif start + 1 == end:
#         if list[start] < list[end]:
#             return list[end], list[start]
#         else:
#             return list[start], list[end]
#     # Find mid of list to break in half and recursively find max/min for each sublist and compare
#     else:
#         mid = (start + (end - start)//2)
#         left_max_min = max_min(list, start, mid)
#         right_max_min = max_min(list, mid+1, end)
#
#         if left_max_min[0] > right_max_min[0]:
#             max = left_max_min[0]
#         else:
#             max = right_max_min[0]
#
#         if left_max_min[1] < right_max_min[1]:
#             min = left_max_min[1]
#         else:
#             min = right_max_min[1]
#
#     max_Min = [max,min]
#     return max_Min

# Time Complexity O(n)
# Number of Comparisons 3n/2 - 2
def max_min(list, num):
    max, min, i = 0, 0, 0
    if num % 2 != 0:
        max = list[0]
        min = list[0]
        i = 1
    else:
        if list[0] < list[1]:
            max = list[1]
            min = list[0]
        else:
            max = list[0]
            min = list[1]
        i = 2
    while i < num:
        if list[i] < list[i+1]:
            if list[i] < min:
                min = list[i]
            if list[i+1] > max:
                max = list[i+1]
        else:
            if list[i] > max:
                max = list[i]
            if list[i+1] < min:
                min = list[i+1]
        i = i + 2

    maxMin = [max,min]
    return maxMin

def main():
    list = [2,4,9,3,14,7]
    num = len(list)
    ans = max_min(list, num)
    print("(Max,Min) = ", ans)

main()












