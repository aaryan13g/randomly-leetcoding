# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def convert(postorder_left, inorder_left, mid, postorder_right, inorder_right):
            if postorder_left:
                new_node = TreeNode(postorder_left[-1])
                i_mid = inorder_left.index(postorder_left[-1])
                mid.left = new_node
                convert(postorder_left[:i_mid], inorder_left[:i_mid], new_node, postorder_left[i_mid:-1],inorder_left[i_mid + 1:])
            if postorder_right:
                new_node = TreeNode(postorder_right[-1])
                i_mid = inorder_right.index(postorder_right[-1])
                mid.right = new_node
                convert(postorder_right[:i_mid], inorder_right[:i_mid], new_node, postorder_right[i_mid:-1],inorder_right[i_mid + 1:])
        node = TreeNode(postorder[-1])
        i_mid = inorder.index(postorder[-1])
        convert(postorder[:i_mid], inorder[:i_mid], node, postorder[i_mid: -1],inorder[i_mid + 1:])
        return node
