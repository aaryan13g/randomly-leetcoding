# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def convert(preorder_left, inorder_left, mid, preorder_right, inorder_right):
            if preorder_left:
                new_node = TreeNode(preorder_left[0])
                i_mid = inorder_left.index(preorder_left[0])
                mid.left = new_node
                convert(preorder_left[1:1 + i_mid], inorder_left[:i_mid], new_node, preorder_left[i_mid + 1:],inorder_left[i_mid + 1:])
            if preorder_right:
                new_node = TreeNode(preorder_right[0])
                i_mid = inorder_right.index(preorder_right[0])
                mid.right = new_node
                convert(preorder_right[1:1 + i_mid], inorder_right[:i_mid], new_node, preorder_right[i_mid + 1:],inorder_right[i_mid + 1:])
        node = TreeNode(preorder[0])
        i_mid = inorder.index(preorder[0])
        convert(preorder[1:1 + i_mid], inorder[:i_mid], node, preorder[i_mid + 1:],inorder[i_mid + 1:])
        return node
