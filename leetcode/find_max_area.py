def maxArea(height):
    max = 0
    nums = len(height)
    for i in range(nums):
        begin = height[0]
        del height[0]
        for i in range(len(height)):
            if height[i] > begin:
                max = max if max > begin * (i + 1) else begin * (i + 1)
            else:
                max = max if max > height[i] * (i + 1) else height[i] * (i + 1)
    return max


print(maxArea([1,8,6,2,5,4,8,3,7]))