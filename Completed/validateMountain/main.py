# Problem Spec: Given an array of list[] of n integers,
# Write a program to check if the given array is a valid mountain or not
# The array list[] is a mountain array if and only if n >= 3 and there exists some i (0 < i < n-1)
# Such that: list[0] < list[1] < ... list[i-1] < list[i] and list[i] > list[i+1] >...> list[n-1]
# Therefore, a valid mountain is when it is first strictly inc. and then strictly dec.

def findMountain(list, numOfElements):
    i = 0
    while list[i] < list[i+1]:  # Strictly increasing
        i += 1
    for j in range(i, numOfElements-1):
        if not list[j] > list[j+1]:  #Strictly decreasing
            return False

    return True


def main():
    list = [1, 4, 6, 8, 10, 5, 4, 2]
    numOfElements = len(list)
    ans = findMountain(list, numOfElements)
    print(ans)
main()