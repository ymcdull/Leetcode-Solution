# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} k
    # @return {integer}
    def kthSmallest(self, root, k):
        stack = []
        count = 0
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                count += 1
                if count == k:
                    return root.val
                root = root.right
        
            
                
                
        
