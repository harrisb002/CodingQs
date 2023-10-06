# This file contains the implementation of the insertion sort algorithm
# Insertion sort works by sorting the values as one does with cards
# Each next value is taken from the unsorted list and compared to the values on the left of it in the list
# The value is inserted into its correct position in the "sorted list" beginning from the start of the list

def insertion_sort(list, numOfElements):
    for i in range(1, numOfElements):  # Choose next element from unsorted list
        curr_value = list[i]  # Store the current value being inserted
        j = i - 1   # Start search for its position starting at the end of the current sorted portion of list
        # Comparing from left to right until current value is less than the value in j position in list
        while(j >= 0 and list[j] > curr_value):
            list[j+1] = list[j]  # If value in list[j] is larger,then insert that value in front of curr value idx
            j -= 1  # Decrement j so the current value will be placed before the greater number appended above
        # Value is inserted in front of value, in sorted list section on the left,
        # if current value exceeds the far right value it is being compared to
        list[j+1] = curr_value

    print(list)

def main():
    list = [1,4,52,53,34,74,13,45,76,87,100,30]
    num = len(list)
    insertion_sort(list,num)

main()