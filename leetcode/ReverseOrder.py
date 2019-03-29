# # 反转列表法
# a = 'abcdef'
# b = list(a)
# b.reverse()
# b = ''.join(b)
# print(b)
#
# # 循环反向迭代法
# a = 'abcdef'
# b = ''
# for i in a:
#     b = i + b
# print(b)
#
# # 反向循环迭代法
# a = 'abcdef'
# b = ''
# for i in a[::-1]:
#     #b = b + i
#     b += i
# print(b)
#
# # 倒序切片法
# a = 'abcdef'
# b = a[::-1]
# print(b)
#
# # 遍历索引法
# a = 'abcdef'
# b = ''
# for i in range(1,len(a)+1):
#     b = b + a[-i]
# print(b)
#
# # 列表弹出法
# a = 'abcdef'
# a = list(a)
# b = ''
# while len(a) > 0:
#     b = b + a.pop()
# print(b)
#
# # 列表解析式法
# a = 'abcdef'
# b = ''.join(i for i in a[::-1])
# print(b)
#
# # 反向遍历索引法
# a = 'abcdef'
# b = ''.join(i for i in a[::-1])
# print(b)
#
# # 累积相加法
# a = 'abcdef'
# from functools import reduce
# def f(x,y):
#     return y + x
# b = reduce(f,a)
# print(b)
#
# # 匿名函数法
# a = 'abcdef'
# b = reduce(lambda x,y:y+x,a)
# print(b)
#
# # 列表倒序法
# a = 'abcdef'
# a = list(a)
# a.sort(reverse=True)
# b = ''.join(a)
# print(b)
#
# # 双向队列排序法
# a = 'abcdef'
# import collections
# b = collections.deque()
# for i in a:
#     b.appendleft(i)
# b = ''.join(b)
# print(b)
#
# # 双向队列反转法
# a = 'abcdef'
# b = collections.deque()
# b.extend(list(a))
# b.reverse()
# b = ''.join(b)
# print(b)
#
# # 一维数组索引法
# a = 'abcdef'
# import pandas as pd
# b = pd.Series(list(a))
# b = ''.join(b[::-1])
# print(b)
#
# # 函数递归法
# a = 'abcdef'
# def f(a):
#     if len(a) <= 1:
#         return a
#     return a[-1] + f(a[:-1])
# b = f(a)
# print(b)
#
# # 对称交换法
# a = 'abcdef'
# def f(a):
#     a = list(a)
#     if len(a) <=1:
#         return a
#     i = 0
#     length = len(a)
#     while i < length/2:
#         a[i],a[length - 1 - i] = a[length - 1 - i],a[i]
#         i += 1
#     return ''.join(a)
# b = f(a)
# print(b)

# def reverse(x: int) -> int:
#     if x >= 0:
#         flag = True
#     else:
#         flag = False
#         x = -x
#     str_x = str(x)
#     list_x = list(str_x)
#     nums = ''.join(i for i in list_x[::-1])
#     nums = int(nums) if flag == True else -int(nums)
#     print(nums)
#     print(2**31 -1)
#     print(nums > 2 ** 31 - 1)
#     if (nums > 2 ** 31 - 1 or nums < -2 ** 31):
#         return 0
#     return nums
#
# a = 1534236469
# print(reverse(a))


def reverse(x: int) -> int:
    if x < 0:
        return False
    str_x = str(x)
    list_x = list(str_x)
    half = int(len(list_x) / 2)
    for i in range(half):
        if list_x[i] == list_x[-i-1]:
            continue
        else:
            return False
    return True

x = 1223321
print(reverse(x))
