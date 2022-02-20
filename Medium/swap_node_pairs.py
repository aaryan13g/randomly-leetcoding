/* https://leetcode.com/problems/swap-nodes-in-pairs/ */

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        nex = head.next
        start = nex
        prev = None
        while True:
            head.next = head.next.next
            nex.next = head
            if prev:
                prev.next = nex
            head = head.next
            if head is None:
                break
            else:
                prev = nex.next
                if head.next is None:
                    break
                else:
                    nex = head.next
        return start
