# Program Prompt: Given an array of X[] of n integers,
# Where some elements are zero and some elements are non-zero.
# Write a program to move all the zeroes to the end of the array
# Input X[] = [4, 8, 6, 0, 2, 0, 1, 15, 12, 0]
# Output X[] = [4, 8, 6, 2, 1, 15, 12, 0, 0, 0]

# def moveZeroes(list, numOfElements):
#     zeroes = 0
#     zerosList = []
#
#     for i in range(numOfElements):
#         if list[i] != 0:
#             zerosList.append(list[i])
#         else:
#             zeroes += 1
#
#     for i in range(zeroes):
#         zerosList.append(0)
#
#     return zerosList

def moveZeroes(list, numOfElements):
    j = 0
    for i in range(numOfElements):
        if list[i] != 0:
            list[i], list[j] = list[j], list[i]
            j += 1
    return list

def main():
    list = [4, 8, 6, 0, 2, 0, 1, 15, 12, 0]
    numOfElements = len(list)
    ans = moveZeroes(list, numOfElements)
    print(ans)

main()