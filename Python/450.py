from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val == key:
            if not root.left and not root.right:
                return None
            elif root.left and not root.right:
                return root.left
            elif not root.left and root.right:
                return root.right
            else:
                tmp = root.left
                while tmp.right:
                    tmp = tmp.right
                root.val = tmp.val
                root.left = self.deleteNode(root.left, tmp.val)

        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)

        return root


if __name__ == "__main__":
    ex = Solution()

    node_7 = TreeNode(7)
    node_6 = TreeNode(6, None, node_7)
    node_4 = TreeNode(4)
    node_2 = TreeNode(2)
    node_3 = TreeNode(3, node_2, node_4)
    root = TreeNode(5, node_3, node_6)

    sol_node_7 = TreeNode(7)
    sol_node_6 = TreeNode(6, None, sol_node_7)
    sol_node_4 = TreeNode(4)
    sol_node_2 = TreeNode(2, None, sol_node_4)
    sol = TreeNode(5, sol_node_2, sol_node_6)

    res = ex.deleteNode(root, 3)

    def check_equal_tree(head_1, head_2):

        assert head_1.val == head_2.val

        if head_1.left:
            check_equal_tree(head_1.left, head_2.left)
        if head_1.right:
            check_equal_tree(head_1.right, head_2.right)

    check_equal_tree(sol, res)
