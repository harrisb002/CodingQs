# This file contains the implementation of the binary search algorithm in python

def insertion_sort(list, num):
    for i in range(1, num):
        curr_value = list[i]
        j = i - 1
        while j >= 0 and list[j] > curr_value:
            list[j+1] = list[j]
            j = j - 1
        list[j+1] = curr_value
    return list

def binarySearch(list, key):
    start = 0
    end = len(list)
    while start <= end-1:
        middle = (start + end)//2
        if list[middle] == key:
            return key
        if list[middle] < key:
            start = middle + 1
        else:
            end = middle
    return False


def main():
    list = [1,4,52,53,34,74,13,45,76,87,100,29]
    num = len(list)
    sorted_list = insertion_sort(list, num)
    print(sorted_list)
    ans = binarySearch(sorted_list, 45)
    print(ans)

main()