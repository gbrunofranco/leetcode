from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            if root.left:
                self.invertTree(root.left)
            if root.right:
                self.invertTree(root.right)
            root.right, root.left = root.left, root.right
        return root


def list_rep(root, first=False, nodes_list=None):

    if first:
        nodes_list = [root.val]
    if root.left:
        nodes_list.append(root.left.val)
    if root.right:
        nodes_list.append(root.right.val)

    if root.left:
        list_rep(root.left, nodes_list=nodes_list)
    if root.right:
        list_rep(root.right, nodes_list=nodes_list)

    return nodes_list


if __name__ == "__main__":
    ex = Solution()

    node_9 = TreeNode(9)
    node_6 = TreeNode(6)
    node_3 = TreeNode(3)
    node_1 = TreeNode(1)
    node_7 = TreeNode(7, node_6, node_9)
    node_2 = TreeNode(2, node_1, node_3)
    root = TreeNode(4, node_2, node_7)

    solution = [4, 7, 2, 9, 6, 3, 1]
    result = list_rep(ex.invertTree(root), True)
    for idx, elem in enumerate(solution):
        assert elem == result[idx]

    node_3 = TreeNode(3)
    node_1 = TreeNode(1)
    root = TreeNode(2, node_1, node_3)
    solution = [2, 3, 1]
    result = list_rep(ex.invertTree(root), True)
    for idx, elem in enumerate(solution):
        assert elem == result[idx]
