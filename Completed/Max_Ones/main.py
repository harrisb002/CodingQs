# Program Spec: An input array X[] is given where all elements are either 0 or 1.
# Write a program to find the maximum number of consecutive 1's in the binary array
# Input: X[] = [1,1,0,1,1,1,0,0,1] -> Output: 3

def max_ones(list):
    num = len(list)
    max_one = 0
    ones = 0
    curr_value = list[0]
    for i in range(num):
        if list[i] == 1:
            ones += 1
        else:
            max_one = max(max_one, ones)
            ones = 0
    return max_one

def main():
    list = [1,1,0,1,1,1,0,0,1]
    ans = max_ones(list)
    print(ans)

main()