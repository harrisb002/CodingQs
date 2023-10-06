# Program prompt: Write a program that takes a sorted array
# Removes all duplicate elements

def removeDuplicates(list, numOfElements):
    new_list = []
    new_list.append(list[0])
    j = 0
    for i in range(numOfElements - 1):
        if list[i+1] != list[i]:
            new_list.append(list[i+1])
            j += 1

    return new_list

def main():
    list = [1, 1, 2, 3, 3, 4, 5, 6, 6, 7, 8, 8]
    num = len(list)
    new_list = removeDuplicates(list, num)
    print(new_list)



main()