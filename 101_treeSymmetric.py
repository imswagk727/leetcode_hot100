# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


#
def isSymmetric(root: Optional[TreeNode]) -> bool:
    return isMirror(root.left, root.right)


def isMirror(left, right):
    # 递归函数，判断左右子树是否对称
    
    # 递归终止条件
    if left is None and right is None:
        # 左右都为空 -> 对称
        return True
    if left is None or right is None:
        # 有一个不为空 -> 不对称
        return False
    # 当前节点value相等 and  左左子树和右右子树 and 左右子树和右左子树
    return (left.val == right.val) and isMirror(left.left, right.right) and isMirror(left.right, right.left)


#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

print(isSymmetric(root))
