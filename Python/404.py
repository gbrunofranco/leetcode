from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        total = 0

        def count(head):
            if head.left:
                if head.left.left is None and head.left.right is None:
                    nonlocal total
                    total += head.left.val
                else:
                    count(head.left)
            if head.right:
                count(head.right)
        count(root)
        return total


if __name__ == "__main__":
    ex = Solution()

    node_7 = TreeNode(7)
    node_15 = TreeNode(15)
    node_20 = TreeNode(20, node_15, node_7)
    node_9 = TreeNode(9)
    root = TreeNode(3, node_9, node_20)

    assert ex.sumOfLeftLeaves(root) == 24

    node_3 = TreeNode(3)
    node_2 = TreeNode(2)
    root = TreeNode(1, node_2, node_3)

    assert ex.sumOfLeftLeaves(root) == 2

    node_0 = TreeNode(0)
    node_5 = TreeNode(5)
    node_1 = TreeNode(1)
    node_9 = TreeNode(9, node_5, node_1)
    root = TreeNode(4, node_9, node_0)

    assert ex.sumOfLeftLeaves(root) == 14
