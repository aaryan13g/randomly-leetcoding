/* https://leetcode.com/contest/weekly-contest-281/problems/merge-nodes-in-between-zeros/ */

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newlist = ListNode()
        start = newlist
        temp = 0
        while True:
            head = head.next
            if head.val == 0:
                newlist.val = temp
                temp = 0
                if head.next == None:
                    break
                else:
                    newlist.next = ListNode()
                    newlist = newlist.next
            else:
                temp += head.val
        return start
