/* https://leetcode.com/problems/remove-nth-node-from-end-of-list/ */

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr = head
        lenn = 0
        while ptr:
            ptr = ptr.next
            lenn += 1
        prev = None
        ptr = head
        start = head
        nex = ptr.next
        if lenn - n == 0:
            start = start.next
            return start
        for i in range(1, lenn - n + 1):
            prev = ptr
            ptr = ptr.next
            nex = ptr.next
        prev.next = nex
        return start
