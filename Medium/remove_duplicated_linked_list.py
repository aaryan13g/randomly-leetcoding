# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        start = head
        end = head
        newlist = ListNode(-123)
        prev = newlist
        res = newlist
        while start is not None:
            cnt = 0
            while end is not None and start.val == end.val:
                cnt += 1
                end = end.next
            if cnt == 1:
                newlist.val = start.val
                prev = newlist
                newlist.next = ListNode(-123)
                newlist = newlist.next
            start = end
        if prev == newlist:
            return None
        if newlist.val == -123:
            prev.next = None
        return res
