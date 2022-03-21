# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = head
        while start:
            cur = start
            cur_val = cur.val
            start = start.next
            while start and start.val == cur.val:
                start = start.next
            cur.next = start
        return head
