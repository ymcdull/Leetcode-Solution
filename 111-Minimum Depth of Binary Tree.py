# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        ### Recursion
        # if not root:
        #     return 0
        # if not root.left:
        #     return self.minDepth(root.right) + 1
        # if not root.right:
        #     return self.minDepth(root.left) + 1
        # return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        
        
        ### Use queue method
        if not root:
            return 0
        
        queue = [root]
        curNode = 1
        nextNode = 0
        level = 1
        
        while queue:
            root = queue.pop(0)
            curNode -= 1
            
            if not root.left and not root.right:
                return level 
            
            if root.left:
                nextNode += 1
                queue.append(root.left)
            if root.right:
                nextNode += 1
                queue.append(root.right)
                
            if curNode == 0:
                curNode = nextNode
                nextNode = 0
                level += 1    
