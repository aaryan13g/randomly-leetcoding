# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def convert(left, mid, right):
            if left:
                left_mid = len(left) // 2
                new_node = TreeNode(left[left_mid])
                mid.left = new_node
                convert(left[:left_mid], new_node, left[left_mid + 1:])
            if right:
                right_mid = len(right) // 2
                new_node = TreeNode(right[right_mid])
                mid.right = new_node
                convert(right[:right_mid], new_node, right[right_mid + 1:])
        mid = len(nums) // 2
        node = TreeNode(nums[mid])
        convert(nums[:mid], node, nums[mid + 1:])
        return node
