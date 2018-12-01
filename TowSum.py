# 给出一个数字列表和一个目标值（target），假设列表中有且仅有两个数相加等于目标值，
# 我们要做的就是找到这两个数，并返回他们的索引值。

def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    result = []
    for i in range(len(nums)):
       oneNum = nums[i]
       twoNum  = target - oneNum
       if twoNum in nums:
          j = nums.index(twoNum)
          if i != j:
             result.append(i)
             result.append(j)
             return result

def twoSum_faster(self, nums, target):
    """
    通过创建字典，将nums里的值和序号对应起来，并创建另一个字典存储目标值（Target）-nums的值，
    通过判断该值是否在nums内进行判断并返回其对应索引值
    哈希算法的应用。
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # 创建字典一，存储输入列表的元素值和对应索引
    num_dict = {nums[i]: i for i in range(len(nums))}
    print(num_dict)
    # 创建另一个字典，存储target-列表中的元素的值，小詹称为num_r吧，好表达
    num_dict2 = {i: target - nums[i] for i in range(len(nums))}
    print(num_dict2)
    # 判断num_r是否是输入列表中的元素，如果是返回索引值，不是则往下进行
    result = []
    for i in range(len(nums)):
        j = num_dict.get(num_dict2.get(i))
        if (j is not None) and (j != i):
            result = [i, j]
            break
    return result