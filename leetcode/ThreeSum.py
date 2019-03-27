# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，
# 使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
def threeSum(nums):
    """
    :type nums: List[int]
    :return: List[List[int]]
    """
    res = []
    nums.sort()
    # 固定一个数。另外两个来匹配，凑0
    for i in range(0, len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        target = 0 - nums[i]
        start, end = i + 1, len(nums) - 1
        while start < end:
            if nums[start] + nums[end] > target:
                end -= 1
            elif nums[start] + nums[end] < target:
                start += 1
            else:
                res.append([nums[i], nums[start], nums[end]])
                end -= 1
                start += 1
                while start < end and nums[end] == nums[end + 1]:
                    end -= 1
                while start < end and nums[start] == nums:
                    start += 1
    return res

if __name__ == '__main__':
    arr = [-1,0,1,2,-1,-4]
    print(threeSum(arr))
