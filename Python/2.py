from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        count_1, count_2 = [], []

        while l1 or l2:
            if l1 and l2:
                count_1.append(l1.val)
                count_2.append(l2.val)
                l1 = l1.next
                l2 = l2.next
            elif l1 and not l2:
                count_1.append(l1.val)
                l1 = l1.next
            elif l2 and not l1:
                count_2.append(l2.val)
                l2 = l2.next

        res_1 = int("".join(map(str, count_1[::-1])))
        res_2 = int("".join(map(str, count_2[::-1])))
        tot_str = str(res_1 + res_2)
        return self.create_list(list(map(int, tot_str[::-1])))

    def create_list(self, value_list):
        if len(value_list) > 0:
            return ListNode(value_list[0], self.create_list(value_list[1:]))
        else:
            return None


if __name__ == "__main__":
    ex = Solution()

    l1_node3 = ListNode(val=3)
    l1_node4 = ListNode(val=4, next=l1_node3)
    l1_root = ListNode(val=2, next=l1_node4)

    l2_node4 = ListNode(val=4)
    l2_node6 = ListNode(val=6, next=l2_node4)
    l2_root = ListNode(val=5, next=l2_node6)

    sol_node8 = ListNode(val=8)
    sol_node0 = ListNode(val=0, next=sol_node8)
    sol = ListNode(val=7, next=sol_node0)

    res = ex.addTwoNumbers(l1_root, l2_root)

    while sol:
        assert sol.val == res.val
        sol, res = sol.next, res.next

    l1_root = ListNode(val=0)
    l2_root = ListNode(val=0)
    sol = ListNode(val=0)
    res = ex.addTwoNumbers(l1_root, l2_root)

    while sol:
        assert sol.val == res.val
        sol, res = sol.next, res.next

    l1 = ex.create_list([2, 4, 9])
    l2 = ex.create_list([5, 6, 4, 9])

    res = ex.addTwoNumbers(l1, l2)
    sol = ex.create_list([7, 0, 4, 0, 1])
    while res:
        assert res.val == sol.val
        sol, res = sol.next, res.next
