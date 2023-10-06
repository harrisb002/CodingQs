# Program Spec: Given an array of integers that is initially inc. and then dec.
# Find the maximum value in the array

def max_middle(list):
    i = 0
    while list[i] < list[i+1]:
        i+=1
    print(list[i])

def main():
    list = [1, 2, 3, 5, 32, 55, 8, 4, 2]
    max_middle(list)

main()