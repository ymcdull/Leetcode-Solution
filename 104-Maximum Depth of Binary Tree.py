# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ### recursion
        
        # if not root:
        #     return 0
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
        
        ### use queue
        if not root:
            return 0
        
        level = 0
        curNode = 1
        nextNode = 0
        
        queue = []
        queue.append(root)
        
        while queue:
            root = queue.pop(0)
            curNode -= 1
            if root.left:
                queue.append(root.left)
                nextNode += 1
            if root.right:
                queue.append(root.right)
                nextNode += 1
            
            if curNode == 0:
                curNode = nextNode
                nextNode = 0
                level += 1
                
        return level
        
        
