from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return
        root = ListNode(val=val+1, next=head)
        base = root

        while root and root.next:

            if root.next.val == val:
                if root.next.next:
                    root.next = root.next.next
                    continue
                else:
                    root.next = None
            root = root.next

        return base.next


if __name__ == "__main__":
    ex = Solution()

    list_node6 = ListNode(val=6)
    list_node7 = ListNode(val=7, next=list_node6)
    root = ListNode(val=7, next=list_node7)

    sol = ListNode(val=6, next=None)

    res = ex.removeElements(root, 7)

    while sol:
        assert sol.val == res.val
        sol, res = sol.next, res.next
