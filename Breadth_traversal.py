# for child in current.children:
#     que.append(child)
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

#  N 叉树的层次遍历 90.36%
class Solution_low(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        que = []
        res = []
        que.append(root)
        while len(que):
            l = len(que)
            sub = []
            for i in range(l):
                current = que.pop(0)
                sub.append(current.val)
                for child in current.children:
                    que.append(child)
            res.append(sub)
        return res

# 运行效率：99.76%
class Solution_fast(object):
    def levelOrder(self, root):
        if not root:
            return []
        ret = []
        ret.append(root)
        ret2 = []
        while len(ret) != 0:
            temp = []
            length = len(ret)
            for index in range(length):
                tempValue = ret.pop(0)
                temp.append(tempValue.val)
                if tempValue.left is not None:
                    ret.append(tempValue.left)
                if tempValue.right is not None:
                    ret.append(tempValue.right)
            ret2.append(temp)
        return ret2

if __name__ == '__main__':
    s1 = Solution_low()
    s2 = Solution_fast()
    list_num = [[3, 9, 20, None, None, 15, 7]]
    res1 = s1.levelOrder(list_num)
    res2 = s2.levelOrder(list_num)
    print(s1)
    print(s2)