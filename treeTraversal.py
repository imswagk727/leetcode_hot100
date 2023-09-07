from typing import List


def inorderTraversal(self, root) -> List[int]:
    if not root:
        return []
    # 前序遍历（preorder），出栈顺序：根左右; 入栈顺序：右左根
    # return [root.val] + self.inorderTraversal(root.left) + self.inorderTraversal(root.right)

    # 中序遍历（inorder），出栈顺序：左根右; 入栈顺序：右根左
    return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

    # 后序遍历（postorder），出栈顺序：左右根; 入栈顺序：根右左
    # return self.inorderTraversal(root.left) + self.inorderTraversal(root.right) + [root.val]
