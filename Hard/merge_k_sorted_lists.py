/* https://leetcode.com/problems/merge-k-sorted-lists/ */

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minn = 100000
        min_head = None
        idx = 0
        for i in range(len(lists) - 1, -1, -1):
            if lists[i] is None:
                lists.pop(i)
        for i in range(len(lists)):
            if lists[i] and lists[i].val < minn:
                minn = lists[i].val
                min_head = lists[i]
                idx = i
        if min_head is None:
            return None
        new_list = ListNode()
        start = new_list
        while True:
            new_list.val = min_head.val
            min_head = min_head.next
            if min_head is None:
                lists.pop(idx)
            else:
                lists[idx] = lists[idx].next
            for i in range(len(lists)):
                if lists[i] and (min_head is None or lists[i].val < min_head.val):
                    min_head = lists[i]
                    idx = i
            if min_head:
                new_list.next = ListNode()
                new_list = new_list.next
            else:
                break
        return start
