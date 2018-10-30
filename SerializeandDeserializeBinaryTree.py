"""
设计一个算法。支持：
1.将二叉树以某种方式转化为一字符串;
2.将字符串逆转化为二叉树

你需要保证将二叉树转化为字符串, 再将该字符串逆转化为二叉树, 得到的二叉树与原二叉树相同。
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        s = []
        def dfs(rt):
            if rt is None:
                s.append(str(rt))
                return
            s.append(str(rt.val))
            dfs(rt.left)
            dfs(rt.right)
        dfs(root)
        return " ".join(s)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        self.pos = -1
        s = data.split()
        def dfs():
            self.pos += 1
            if s[self.pos] == str(None): return None
            node = TreeNode(int(s[self.pos]))
            node.left = dfs()
            node.right = dfs()
            return node
        root = dfs()
        return root

 # Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))