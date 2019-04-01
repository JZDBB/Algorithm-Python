
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
    if l % 2 == 0:
        return float((num[l // 2 - 1] + num[l // 2]) / 2)
    else:
        return float(num[l // 2])