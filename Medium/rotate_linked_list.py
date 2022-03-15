# https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        st = head
        last = None
        while st:
            n += 1
            last = st
            st = st.next
        if n < 2:
            return head
        k = k % n
        if k == 0:
            return head
        else:
            start = head
            for i in range(n - k - 1):
                start = start.next
            last.next = head
            first = start.next
            start.next = None
            return first
            
