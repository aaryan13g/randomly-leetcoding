# https://leetcode.com/problems/copy-list-with-random-pointer/

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        newlist = ListNode()
        start = newlist
        orig = head
        while True:
            start.val = orig.val
            orig = orig.next
            if orig:
                start.next = ListNode()
                start = start.next
            else:
                break
        orig = head
        start = newlist
        while orig:
            rand = orig.random
            orig_st = head
            new_st = newlist
            while rand != orig_st:
                orig_st = orig_st.next
                new_st = new_st.next
            start.random = new_st
            start = start.next
            orig = orig.next
        return newlist
