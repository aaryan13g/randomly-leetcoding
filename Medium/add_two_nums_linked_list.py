/* https://leetcode.com/problems/add-two-numbers/ */

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num = []
        carry = 0
        head = ListNode()
        l = head
        while True:
            if l1 is None and l2 is None and carry == 0:
                break
            d1, d2 = 0, 0
            if l1 is not None:
                d1 = l1.val
                l1 = l1.next
            if l2 is not None:
                d2 = l2.val
                l2 = l2.next
            sm = d1 + d2 + carry
            digit = sm % 10
            carry = sm // 10
            num.append(digit)
            l.next = ListNode()
            l = l.next
            l.val = digit
            
        return head.next
