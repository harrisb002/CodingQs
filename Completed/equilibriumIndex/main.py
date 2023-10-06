# Prompt: Write a program to find the equilibrium index of an array.
# The equilibrium index is an index such that the elements at the
# Lower indexes is equal to the sum of the elements at higher indexes.
# Therefore, with i = equilibrium index:
# A[0] + A[1] + .....+ A[i-1] = A[i+1] + .....+ A[n-1], Where 0 <= i <= n-1

# Assumptions: Element at index i is not included in either left or right part
# Max of one equilibrium value
# Input values may be repeated and pos./neg.

# Brute fource technique:
# def findIndex(list, numOfElements):
#     leftsum = 0
#     rightsum = 0
#
#     for i in range(numOfElements):
#         leftsum = 0
#         for j in range(i):
#             leftsum += list[j]
#
#         rightsum = 0
#         for j in range(i+1, numOfElements):
#             rightsum += list[j]
#
#         if leftsum == rightsum:
#             return i
#
#     return -1


# # Using a prefix sum array and single loop
# # First declare prefix sum array of size n, then traverse array to store prefix sum
# def findIndex(list, numOfElements):
#     prefix = [0] * numOfElements  # Load 0 for numOfElements
#
#     # Load prefix with sums from 0 to index
#     for i in range(numOfElements):
#         if i == 0:
#             prefix[i] = list[i]  # Load first integer
#         else:
#             prefix[i] = list[i] + prefix[i-1]  # Find sum for every index that follows until numOfElements is reached
#
#     totalSum = prefix[numOfElements-1]  # Total sum is the last index in the prefix array
#
#     for i in range(numOfElements):
#         leftSum = prefix[i] - list[i]
#         rightSum = totalSum- prefix[i]
#         if leftSum == rightSum:
#             return i
#     return -1

# Using single loop method
def findIndex(list, numOfElements):
    totalSum = 0
    leftSum = 0
    for i in range(numOfElements):  # Find total sum of elements
        totalSum += list[i]

    for i in range(numOfElements):
        rightSum = totalSum - leftSum - list[i]
        if leftSum == rightSum:
            return i
        leftSum += list[i]
    return -1

def main():
    list = [-7 ,1 ,5 ,2 ,-4 ,3 ,0]  #EQ index = 3
    num = len(list)
    eqIdx = findIndex(list,num)
    print(eqIdx)

main()