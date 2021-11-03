from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def count(head, values=None):
            if values is None:
                values = list()

            if head.left is None and head.right is None:
                values.append(head.val)
                tmp = 0
                for idx, val in enumerate(values[::-1]):
                    tmp += val * 10**idx
                return tmp

            part = 0

            if head.left:
                part += count(head.left, values + [head.val])

            if head.right:
                part += count(head.right, values + [head.val])

            return part

        return count(root)


if __name__ == "__main__":
    ex = Solution()
    node_3 = TreeNode(3)
    node_2 = TreeNode(2)
    root = TreeNode(1, node_2, node_3)

    assert ex.sumNumbers(root) == 25

    node_0 = TreeNode(0)
    node_5 = TreeNode(5)
    node_1 = TreeNode(1)
    node_9 = TreeNode(9, node_5, node_1)
    root = TreeNode(4, node_9, node_0)

    assert ex.sumNumbers(root) == 1026
