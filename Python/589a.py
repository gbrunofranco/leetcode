from typing import List


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        representation = []
        self.depth_first(root, representation)
        return representation

    def depth_first(self, root, representation):
        if root is None:
            return

        output.append(root.val)
        for child in root.children:
            self.depth_first(child, output)