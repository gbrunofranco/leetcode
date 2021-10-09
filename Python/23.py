from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        values = list()
        for linked_list in lists:
            while linked_list:
                values.append(linked_list.val)
                linked_list = linked_list.next

        return self.create_linked_list(sorted(values))

    def create_linked_list(self, values):
        if values:
            return ListNode(val=values[0], next=self.create_linked_list(values[1:]))
        else:
            return None


if __name__ == "__main__":
    ex = Solution()

    node6 = ListNode(6)
    root3 = ListNode(2, node6)

    node4 = ListNode(4)
    node3 = ListNode(3, node4)
    root2 = ListNode(1, node3)

    node5 = ListNode(5)
    node4 = ListNode(4, node5)
    root1 = ListNode(1, node4)

    returned_list = ex.mergeKLists([root1, root2, root3])
    idx = 0
    sol = [1, 1, 2, 3, 4, 4, 5, 6]
    while returned_list:
        assert returned_list.val == sol[idx]
        returned_list, idx = returned_list.next, idx+1
