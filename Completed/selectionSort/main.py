# This file contains the implementation of the selection sort algorithm
# Selection sort works by finding the next smallest number in list and inserting it
# In front of the last minimum value in list found, stating at index 0

def selection_sort(list, numOfElements):
    for i in range(numOfElements - 1):
        min_idx = i
        for j in range(i, numOfElements):
            if list[j] < list[min_idx]:
                min_idx = j

        list[i], list[min_idx] = list[min_idx], list[i]

    print(list)


def main():
    list = [3, 5, 1, 2, 43, 33, 14, 235, 63, 74, 23, 75, 34, 44, 99]
    num = len(list)
    selection_sort(list, num)


main()
