# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        cur = head
        sum = 0
        while cur:
            if cur.val + sum == 0:
                dummy.next = cur.next
            sum += cur.val
            cur = cur.next
        if dummy.next:
            dummy.next.next = self.removeZeroSumSublists(dummy.next.next)
        return dummy.next
