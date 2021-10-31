class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        detatched = []
        root = head
        while head:
            if head.child:
                if head.next is not None:
                    detatched.append(head.next)
                head.next = head.child
                head.child = None
                head.next.prev = head
                head = head.next
            elif head.next is not None or len(detatched) == 0:
                head = head.next
            elif head.next is None or len(detatched) != 0:
                head.next = detatched.pop(-1)
                head.next.prev = head
                head = head.next
        return root


if __name__ == "__main__":
    ex = Solution()

    node_12 = Node(12, None, None, None)
    node_11 = Node(11, None, node_12, None)
    node_10 = Node(10, None, None, None)
    node_9 = Node(9, None, node_10, None)
    node_8 = Node(8, None, node_9, node_11)
    node_7 = Node(7, None, node_8, None)
    node_6 = Node(6, None, None, None)
    node_5 = Node(5, None, node_6, None)
    node_4 = Node(4, None, node_5, None)
    node_3 = Node(3, None, node_4, node_7)
    node_2 = Node(2, None, node_3, None)
    root = Node(1, None, node_2, None)

    node_12.prev = node_11
    node_10.prev = node_9
    node_9.prev = node_8
    node_8.prev = node_7
    node_6.prev = node_5
    node_5.prev = node_4
    node_4.prev = node_3
    node_3.prev = node_2
    node_2.prev = root

    res = ex.flatten(root)
    idx = 0
    sol = [1, 2, 3, 7, 8, 11, 12, 9, 10, 4, 5, 6]
    while res:
        assert res.val == sol[idx]
        res, idx = res.next, idx+1
