# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def _k_possible(node, p):
            if node and not p:
                return node
            elif not node:
                return False
            else:
                return _k_possible(node.next, p-1)
        # the function keeps the one after k nodes the same
        tail, previous = head, head
        if not _k_possible(tail, k-1):
            return tail
        if tail:
            current = head.next
        else:
            current = None
        iterations = k - 1
        while current and iterations:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
            iterations -= 1
        if tail:
            tail.next = self.reverseKGroup(current, k)

        return previous
