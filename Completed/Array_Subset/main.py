# Program Spec: Given two unsorted arrays X[] and Y[] of size m and n respectively
# Write a program to check whether array Y[] is a subset of array X[] or not.
# Y[] will be a subset of X[] if each element of Y[] is present in X[].
# Assume that there are no repeated elements in both arrays and n <= m
# Input: X[] = [2,8,12,6,10,11]  Y[] = [8,2,6,11]  -> Output: True

def check_subset(X, Y, m, n):
    X = insertionSort(X, m)  # Sort list X, thus can use binary search
    for i in range(0, n):
        key = binarySearch(X, 0, m-1, Y[i])  # Search list X for element at Y[i] in subset list
        if key == -1:
            return False
    return True

def binarySearch(list, start, end, key):
    while(start <= end):
        middle = (start + (end-1))//2
        if(list[middle] == key):
            return key
        if(list[middle] < key):
            start = middle + 1
        else:
            end = middle
    return -1

#Implements insertion sort algorithm
def insertionSort(list, numOfElements):
    for i in range(1, numOfElements):
        curr_value = list[i]
        j = i - 1
        while(j >= 0 and list[j] > curr_value):
            list[j+1] = list[j]
            j-= 1
        list[j+1] = curr_value
    return list

def main():
    X = [2,8,12,6,78,11,5,88,10]
    Y = [8,2,12,10]
    m = len(X)
    n = len(Y)
    ans = check_subset(X, Y, m, n)
    print(ans)

main()