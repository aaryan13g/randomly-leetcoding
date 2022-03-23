# https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        beforeleft, cur = None, head
        i = 1
        while i < left:
            beforeleft = cur
            cur = cur.next
            i += 1
        first = cur
        prev = None
        nex = None
        while i <= right:
            nex = cur.next
            cur.next = prev
            prev = cur
            cur = nex
            i += 1
        first.next = nex
        if beforeleft:
            beforeleft.next = prev
        else:
            head = prev
        return head
