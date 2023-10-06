# Program spec: Given an unsorted array list[] of distinct elements
# Write a program to find the maximum difference between a pair of indices
# Such that the larger value appears after the element with the smaller value
# I:e j > i and list[j] > list[i]
# Assume that all values in the input are distinct
# There can be several suh pairs of indices for which the difference will be maximum
# Only need to return the max difference between j-i
# Input: list[] = [1,2,3,4,5,6] -> Output: 5
# Input: list[] = [7,6,5,4,3,2] -> Output: -1
# Input: list[] = [40,20,70,10,-20,80,30,-10] -> Output: 5

def findMaximum(list, num):
    LeftMin = [0] * num
    RightMax = [0] * num

    LeftMin[0] = list[0]
    for i in range(1, num):
        LeftMin[i] = min(list[i], LeftMin[i-1])

    RightMax[num-1] = list[num-1]
    for j in range(num-2, -1, -1):
        RightMax[j] = max(list[j], RightMax[j+1])

    i = 0
    j = 0
    maxDiff = -1

    while j < num and i < num:
        if LeftMin[i] <= RightMax[j]:
            maxDiff = max(maxDiff, j-1)
            j = j + 1
        else:
            i = i + 1

    # When array is sorted in decreasing order
    if maxDiff == 0:
        return -1
    else:
        return maxDiff


def main():
    list = [4,9,2,12,3,8,7,1]
    num = len(list)
    ans = findMaximum(list, num)
    print(ans)

main()

