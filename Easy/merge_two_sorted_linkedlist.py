/* https://leetcode.com/problems/merge-two-sorted-lists/ */

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        min_head, other_head = None, None
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val < list2.val:
            min_head = list1
            other_head = list2
        else:
            min_head = list2
            other_head = list1
        newlist = ListNode()
        start = newlist
        while min_head is not None:
            while min_head is not None and (other_head is None or min_head.val <= other_head.val):
                print("Inside loop", min_head.val)
                newlist.val = min_head.val
                min_head = min_head.next
                if min_head is None and other_head is None:
                    break
                newlist.next = ListNode()
                newlist = newlist.next
            temp = min_head
            min_head = other_head
            other_head = temp
        return start
