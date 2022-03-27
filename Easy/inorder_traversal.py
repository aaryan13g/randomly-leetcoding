# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def traverse(node, ans):
            if not node:
                return
            traverse(node.left, ans)
            ans.append(node.val)
            traverse(node.right, ans)
            return ans
        return traverse(root, [])
    
        # if not root:
        #     return []
        # else:
        #     return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
