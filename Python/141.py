class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        receivers = set()
        while head:
            if head in receivers:
                return True
            receivers.add(head)
            head = head.next
        return False
