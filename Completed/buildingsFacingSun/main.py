# Problem Spec: Given an input array height[] representing the heights of buildings,
# Write a program to count the number of buildings facing the sun, all building have distinct sizes
# Ex: height [] = [7, 4, 8, 2, 9] = 3 --> As 7 blocks 4 and 8 blocks 2

def facingSun(list, numOfBuildings):
    maxHeight = list[0]  # Initialize max height as first building
    ans = 1     # First building always faces sun

    for i in range(1, numOfBuildings):
        if list[i] > maxHeight:
            maxHeight = list[i]  # If new max height of building found, update max height
            ans += 1
    return ans

def main():
    height = [7, 4, 8, 2, 9]
    numOfBuildings = len(height)
    ans = facingSun(height, numOfBuildings)
    print(ans)

main()



