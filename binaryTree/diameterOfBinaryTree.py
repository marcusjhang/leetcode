# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(root, result):
            if not root:
                return 0
            
            l, r = height(root.left, result), height(root.right, result)

            diameter = l + r
            if diameter > result[0]:
                result[0] = diameter

            return max(l, r) + 1
        
        result = [0]
        height(root, result)
        return result[0]