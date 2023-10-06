# This is an implementation of the bubble sort algorithm

def bubble_sort(list, numOfElements):
    swap = True
    for i in range (numOfElements):
        swap = False
        for j in range(numOfElements-i-1):
            if list[j] > list[j+1]:  # If num in behind is larger swap
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
                swap = True
        if not swap:
            break
    print(list)

def main():
    list = [1,4,2,5,3,6,24,75,55,57,33,77]
    num = len(list)
    bubble_sort(list, num)



main()