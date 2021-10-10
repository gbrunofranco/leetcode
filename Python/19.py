from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, dummy

        while fast.next:
            if n > 0:
                n -= 1
            else:
                slow = slow.next
            fast = fast.next
        slow.next = slow.next.next

        return dummy.next


if __name__ == "__main__":
    ex = Solution()

    node5 = ListNode(5)
    node4 = ListNode(4, node5)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    root = ListNode(1, node2)

    res = ex.removeNthFromEnd(root, 2)

    sol_node5 = ListNode(5)
    sol_node3 = ListNode(3, sol_node5)
    sol_node2 = ListNode(2, sol_node3)
    sol = ListNode(1, sol_node2)

    while sol:
        assert res.val == sol.val
        res, sol = res.next, sol.next

    node2 = ListNode(2)
    root = ListNode(1, node2)

    res = ex.removeNthFromEnd(root, 2)
    sol = ListNode(2)

    while sol:
        assert res.val == sol.val
        res, sol = res.next, sol.next
