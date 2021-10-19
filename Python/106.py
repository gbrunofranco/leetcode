from typing import List, Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def print_tree(root, string_repr=None):

    if string_repr is None:
        string_repr = []

    if root is not None:
        string_repr.append(root.val)
        print_tree(root.left, string_repr)
        print_tree(root.right, string_repr)

    return string_repr


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        if inorder:
            root = TreeNode(postorder.pop())
            # we can do this because lists are made of unique values
            root_index = inorder.index(root.val)

            root.right = self.buildTree(inorder[root_index+1:], postorder)
            root.left = self.buildTree(inorder[:root_index], postorder)

            return root


if __name__ == "__main__":
    ex = Solution()

    node_7 = TreeNode(7)
    node_15 = TreeNode(15)
    node_20 = TreeNode(20, node_15, node_7)
    node_9 = TreeNode(9)
    root = TreeNode(3, node_9, node_20)

    res = ex.buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])

    string_repr_sol, string_repr_res = print_tree(root), print_tree(res)

    for val_sol, val_res in zip(string_repr_sol, string_repr_res):
        assert val_sol == val_res
