# 定义二叉树
class TreeNode:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left  # 左子树
        self.right = right  # 右子树



# 深度优先
# 前序遍历
def preTraverse(root):
    if root is None:
        return
    print(root.value)
    preTraverse(root.left)
    preTraverse(root.right)

# 中序遍历
def midTraverse(root):
    if root is None:
        return
    midTraverse(root.left)
    print(root.value)
    midTraverse(root.right)

# 后序遍历
def afterTraverse(root):
    if root is None:
        return
    afterTraverse(root.left)
    afterTraverse(root.right)
    print(root.value)

# 广度优先
def levelOrder(root):
    res = []
    # 如果根节点为空，则返回空列表
    if root is None:
        return res
    # 模拟一个队列储存节点
    q = []
    # 首先将根节点入队
    q.append(root)
    # 列表为空时，循环终止
    while len(q) != 0:
        length = len(q)
        for i in range(length):
            # 将同层节点依次出队
            r = q.pop(0)
            if r.left is not None:
                # 非空左孩子入队
                q.append(r.left)
            if r.right is not None:
                # 非空右孩子入队
                q.append(r.right)
            print(r.value)

if __name__ == '__main__':
    # 实例化一个树
    node1 = TreeNode("A", TreeNode("B", TreeNode("D"), TreeNode("E")), TreeNode("C", TreeNode("F"), TreeNode("G")))