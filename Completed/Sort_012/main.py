# Program Spec: Given an array X[] consisting of 0's, 1's, and 2's
# Write a program to sort the array in ascending order
# Note: Solve using a single loop and three-pointers

# Time Complexity: O(n)
# def sort_list(list, num):
#     zeroes = 0
#     ones = 0
#     twos = 0
#     for i in range(num):
#         if list[i] == 0:
#             zeroes += 1
#         elif list[i] == 1:
#             ones += 1
#         elif list[i] == 2:
#             twos += 1
#
#     i = 0
#     while zeroes > 0:
#         list[i] = 0
#         i+=1
#         zeroes -= 1
#     while ones > 0:
#         list[i] = 1
#         i += 1
#         ones -= 1
#     while twos > 0:
#         list[i] = 2
#         i += 1
#         twos -= 1
#
#     return list

# Time Complexity: O(n)
def sort_list(list, num):
    low = 0
    mid = 0
    high = num-1
    while mid <= high:
        if list[mid] == 0:  # If middle index = 0 then swap with low and increment both low and mid
            list[low], list[mid] = list[mid], list[low]
            low += 1
            mid += 1
        elif list[mid] == 1:  # If middle index = 1 then increment mid by 1
            mid += 1
        elif list[mid] == 2:  # If middle index = 2 then swap with high and decrement high by one
            list[mid], list[high] = list[high], list[mid]
            high -= 1

    return list

def main():
    list = [2,0,1,0,2,0,1,2]
    num = len(list)
    ans = sort_list(list, num)
    print(ans)

main()