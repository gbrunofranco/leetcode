from typing import List

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return

        representation = []
        stack = [root]
        
        while stack:
            # Pop from top of the stack version
            new_node = stack.pop()
            representation.append(new_node.val)
            stack.extend(new_node.children[::-1])

            """
            Pop from bottom of the stack version, slightly slower
            
            new_node = stack.pop(0)
            representation.append(new_node.val)
            stack = new_node.children + stack
            """
        return representation