from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        dict_inorder = {v: i for i, v in enumerate(inorder)}
        self.index = 1

        def build(idx_left, idx_right):
            if idx_left > idx_right:
                return None

            root = TreeNode(postorder[-self.index])
            self.index += 1
            idx_root = dict_inorder[root.val]
            root.right = build(idx_root+1, idx_right)
            root.left = build(idx_left, idx_root-1)
            return root

        return build(0, len(inorder)-1)


def print_tree(root, string_repr=None):

    if string_repr is None:
        string_repr = []

    if root is not None:
        string_repr.append(root.val)
        print_tree(root.left, string_repr)
        print_tree(root.right, string_repr)

    return string_repr


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
