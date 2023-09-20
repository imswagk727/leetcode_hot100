from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root: Optional[TreeNode]) -> int:
    # DFS 深度优先搜索
    # 
    # 根结点为空，返回深度0
    if root is None:
        return 0
    # 递归计算 左右子树的最大神深度，加1表示根节点深度。
    return 1 + max(maxDepth(root.left), maxDepth(root.right))


# 创建二叉树
# root = [3,9,20,null,null,15,7]
#     3
#   9 | 20
# N N | 15 7 
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(maxDepth(root))