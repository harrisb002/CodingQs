# Program Spec: Given n non-negative integers representing an elevation map
# Where the width of each tower is 1.
# Write a program to compute how much water it can trap after raining
# Input: height[] = [0,1,0,2,1,0,1,3,2,1,2,1] -> Ouput: 6
# Exp: Trapped water = 1x1 + 1x1 + 2x1 + 1x1 + 1x1 = 6

def trapped_Water(height, n):
    trappedWater = 0
    leftMax = 0
    rightMax = 0
    left = 0
    right = n-1
    while left <= right:
        if height[left] < height[right]:
            if height[left] > leftMax:
                leftMax = height[left]
            else:
                trappedWater = trappedWater + leftMax - height[left]
            left = left + 1
        else:
            if height[right] > rightMax:
                rightMax = height[right]
            else:
                trappedWater = trappedWater + rightMax - height[right]
            right = right - 1

    return trappedWater

def main():
    height = [0,1,0,2,1,0,1,3,2,1,2,1]  # Ouput: 6
    num = len(height)
    water = trapped_Water(height,num)
    print(water)

main()