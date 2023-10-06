# Program Spec: you are given an array x[] consisting of n elements, write a program
# To find the majority element in an array i:e return the number which appears more than n/2 times

def find_majority_element(list, num):
    list = insertion_sort(list, num)
    curr_max = list[0]
    max_count = 0
    next_max = 0
    next_count = 0
    for i in range(num):
        print("Current max:", curr_max)
        print("Current max count:", max_count)
        if next_count > max_count:
            curr_max = next_max
            max_count = next_count
            next_count = 0
        if list[i] == curr_max:
            max_count += 1
        elif list[i] > curr_max:
            if list[i] != next_max:
                next_count = 0
            else:
                next_count += 1
                print("next count:", next_count)
            next_max = list[i]
            print("next max:", next_max)




    return curr_max

def insertion_sort(list, num):
    for i in range(num):
        curr_value = list[i]
        j = i - 1
        while j >= 0 and list[j] > curr_value:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = curr_value
    print(list)
    return list

def main():
    list = [4,3,4,1,3,2,7,1,3,7,6,]
    num = len(list)
    ans = find_majority_element(list, num)
    print(ans)
main()