from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        curr = root
        while curr:
            if curr.left:
                runner = curr.left
                while runner.right:
                    runner = runner.right
                runner.right, curr.right, curr.left = curr.right, curr.left, None
            curr = curr.right

        return root


if __name__ == "__main__":
    ex = Solution()

    node_6 = TreeNode(6)
    node_5 = TreeNode(5, None, node_6)
    node_4 = TreeNode(4)
    node_3 = TreeNode(3)
    node_2 = TreeNode(2, node_3, node_4)
    root = TreeNode(1, node_2, node_5)

    res = ex.flatten(root)
    sol_node6 = TreeNode(6)
    sol_node5 = TreeNode(5, None, sol_node6)
    sol_node4 = TreeNode(4, None, sol_node5)
    sol_node3 = TreeNode(3, None, sol_node4)
    sol_node2 = TreeNode(2, None, sol_node3)
    sol = TreeNode(1, None, sol_node2)

    while res or sol:
        assert res.val == sol.val
        res, sol = res.right, sol.right
