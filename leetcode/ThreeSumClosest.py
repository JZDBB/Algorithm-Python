
def threeSumClosest(nums, target):
    if len(nums) < 3:
        return None
    if len(nums) == 3:
        return sum(nums)

    nums.sort()
    min = nums[0] + nums[1] + nums[2] - target
    res = 0
    for i in range(len(nums) - 2):
        dis = nums[i] + nums[i + 1] + nums[i + 2] - target
        if dis <= min:
            min = dis
            res = nums[i] + nums[i + 1] + nums[i + 2]

    return res


print(threeSumClosest([0,2,1,-3], 1))



