# Program Spec: Given an array of n non-negative integers height[n]
# Where each value represents a point at coordinate (i, height[i])
# Now n vertical lines are drawn such that
# The two endpoints of line i are at (i,0) and (i,height[i]).
# Here each pair of a line with the x-axis forms a container
# Write a program tp find two lines, such that the container
# Contains the most water. Return an int. that corresponds to the
# Maximum area of water that can be contained.
# Notes:
# The value of n is at least 2
# Need to maximize the area formed between the vertical lines using the
# Shorter line as height and the distance between the lines as the width
# I.e Area = max[(j - i) * min( height[i], height[j] ) ]

# Output = 12
# Exp: Max Area = (4-1) * min(height[4],height[1]
# 3 * min(4,5)
# 3 * 4 = 12

# Time Complexity = O(n^2)
# def find_max_area(list, num):
#     max_area = 0
#     for i in range(num):
#         for j in range(i, num):
#             area = (j-i) * min(list[i], list[j])
#             max_area = max(max_area, area)
#     return max_area

# Time Complexity = O(n)
# When height[i] < height[j] it is not necessary to compute (i, j-1), (i,j-2) ect
# Same goes for height[i] > height[j] it is not necessary to compute (i+1, j), (i+2,j) ect
def find_max_area(list, num):
    max_area = 0
    i = 0
    j = num - 1
    while i < j:
        area = (j - i) * min(list[i], list[j])
        max_area = max(max_area, area)
        if list[i] < list[j]:
            i = i + 1
        else:
            j = j - 1
    return max_area



def main():
    height_list = [1, 5, 6, 3, 4, 2]
    num = len(height_list)
    ans = find_max_area(height_list, num)
    print(ans)

main()