# Program Spec: Given a sorted 2D array and an integer k
# Write a program to find whether the integer k is present
# In the matrix or not. The matrix has the following properties:
# Integers in each are sorted from left to right
# The first integer of each row is greater than the last integer of the previous row
# Input: k = 5
# mat[][] =
# [
#     [1,   2,  6,  7],
#     [12, 13, 16, 21],
#     [23, 35, 36, 48]
# ]
# Output: True
# Exp: Value 6 is present in matrix

def findNum(list, k):
    for col in list:
        for row in col:
            if row > k:
                return False
            if k == row:
                return True
    return False



def main():
    list = [[1,   2,  6,  7],
            [12, 13, 16, 21],
            [23, 35, 36, 48]]

    print(findNum(list, 16))

main()

