# https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head
        l_list, l_ptr, r_list, r_ptr = None, None, None, None
        while head:
            node = ListNode(head.val)
            if head.val < x:
                if not l_list:
                    l_list = node
                    l_ptr = l_list
                else:
                    l_ptr.next = node
                    l_ptr = l_ptr.next
            else:
                if not r_list:
                    r_list = node
                    r_ptr = r_list
                else:
                    r_ptr.next = node
                    r_ptr = r_ptr.next
            head = head.next
        if l_ptr:
            l_ptr.next = r_list
        else:
            l_list = r_list
        return l_list
