# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        start = head
        n = 0
        while start:
            n += 1
            start = start.next
        start = head
        node1, node2 = None, None
        for i in range(1, max(k+1, n-k+2)):
            if i == k:
                node1 = start
            if i == n-k+1:
                node2 = start
            start = start.next
        node1.val, node2.val = node2.val, node1.val
        return head
