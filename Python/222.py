from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        left_height, right_height = 0, 0

        if root.left:
            head = root.left
            left_height += 1
            while head.left:
                left_height += 1
                head = head.left

            if root.right:
                right_height += 1
                head = root.right
                while head.left:
                    right_height += 1
                    head = head.left

        if left_height == right_height:
            return pow(2, left_height) + self.countNodes(root.right)
        else:
            return pow(2, right_height) + self.countNodes(root.left)


if __name__ == "__main__":
    ex = Solution()

    node_6 = TreeNode(6)
    node_5 = TreeNode(5)
    node_4 = TreeNode(4)
    node_3 = TreeNode(3, node_6)
    node_2 = TreeNode(2, node_4, node_5)
    root = TreeNode(1, node_2, node_3)
    assert ex.countNodes(root) == 6
