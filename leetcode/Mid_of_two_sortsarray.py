import datetime
def get_Median(nums1, nums2):
    """
    :param list1: a sorted array.
    :param list2:  another sorted array
    :return med: median of concate two array
    """
    l1 = len(nums1)
    l2 = len(nums2)
    l = l1 + l2
    if l == 0:
        return None
    if l == 1:
        if nums1:
            return nums1[-1]
        if nums2:
            return nums2[-1]
    num = []
    i = j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            num.append(nums1[i])
            i += 1
        elif nums1[i] > nums2[j]:
            num.append(nums2[j])
            j += 1
        else:
            num.append(nums1[i])
            num.append(nums2[j])
            i += 1
            j += 1
    while i < len(nums1):
        num.append(nums1[i])
        i += 1
    while j < len(nums2):
        num.append(nums2[j])
        j += 1
    if len(num) > l//2:
        if l % 2 == 0:
            return float((num[l // 2 - 1] + num[l // 2]) / 2)
        else:
            return float(num[l // 2])

def get_Median_long(nums1, nums2):
    """
    :param list1: a sorted array.
    :param list2:  another sorted array
    :return med: median of concate two array
    """
    l1 = len(nums1)
    l2 = len(nums2)
    l = l1 + l2
    if l == 0:
        return None
    if l == 1:
        if nums1:
            return nums1[-1]
        if nums2:
            return nums2[-1]
    num = []
    i = j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            num.append(nums1[i])
            i += 1
        elif nums1[i] > nums2[j]:
            num.append(nums2[j])
            j += 1
        else:
            num.append(nums1[i])
            num.append(nums2[j])
            i += 1
            j += 1
            if len(num) > l // 2:
                if l % 2 == 0:
                    return float((num[l // 2 - 1] + num[l // 2]) / 2)
                else:
                    return float(num[l // 2])
    while i < len(nums1):
        num.append(nums1[i])
        i += 1
        if len(num) > l//2:
            if l % 2 == 0:
                return float((num[l // 2 - 1] + num[l // 2]) / 2)
            else:
                return float(num[l // 2])
    while j < len(nums2):
        num.append(nums2[j])
        j += 1
        if len(num) > l//2:
            if l % 2 == 0:
                return float((num[l // 2 - 1] + num[l // 2]) / 2)
            else:
                return float(num[l // 2])

list1 = [1, 3, 4, 5, 7, 8, 9, 10 , 12, 13, 14, 15, 17, 19, 20, 24, 25, 35, 45, 56, 76, 78, 90, 100]
list2 = [1, 3, 4, 5, 7, 8, 9, 10 , 12, 13, 14, 15, 17, 19, 20, 24, 25, 35, 45, 56, 76, 78, 90, 100]
start_time = datetime.datetime.now()
print(get_Median(list1, list2))
end_time = datetime.datetime.now()  # 放在程序结尾处
interval = (end_time - start_time).seconds  # 以秒的形式
print('final_name:\t', interval)

start_time = datetime.datetime.now()
print(get_Median_long(list1, list2))
end_time = datetime.datetime.now()  # 放在程序结尾处
interval = (end_time - start_time).seconds  # 以秒的形式
print('final_name:\t', interval)