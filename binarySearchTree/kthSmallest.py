# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodes = [] #inorder traversal
        
        def inorderTraversal(root, nodes):
            if not root:
                return
            
            inorderTraversal(root.left, nodes)
            nodes.append(root.val)
            inorderTraversal(root.right, nodes)
        
        inorderTraversal(root, nodes)

        return nodes[k-1]

# T O(n) S O(n)